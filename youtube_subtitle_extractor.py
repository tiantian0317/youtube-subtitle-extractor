#!/usr/bin/env python3
"""
YouTube 字幕提取工具

功能：
- 从 YouTube URL 提取字幕
- 支持多种输出格式（纯文本、JSON、SRT、WebVTT）
- 自动选择最佳语言字幕
- 支持指定语言

使用示例：
    python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID
    python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --lang zh-Hans
    python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --format srt --output subtitle.srt
"""

import re
import sys
import argparse
import json
from typing import Optional
from pathlib import Path

# 添加父目录到 Python 路径，以导入 youtube_transcript_api
script_dir = Path(__file__).parent
parent_dir = script_dir.parent
sys.path.insert(0, str(parent_dir))

# 导入 youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import (
    TextFormatter,
    JSONFormatter,
    SRTFormatter,
    WebVTTFormatter,
)
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    CouldNotRetrieveTranscript,
)


def extract_video_id(url: str) -> str:
    """
    从 YouTube URL 中提取视频 ID

    支持的 URL 格式：
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|m\.youtube\.com\/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',  # 直接输入 video ID
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError(f"无法从 URL 中提取视频 ID: {url}")


def get_transcript(
    video_id: str,
    language: Optional[str] = None,
    languages: Optional[list] = None,
    preserve_formatting: bool = False,
) -> str:
    """
    获取视频字幕

    Args:
        video_id: YouTube 视频 ID
        language: 单个语言代码（如 'zh-Hans'）
        languages: 语言代码列表（按优先级排序）
        preserve_formatting: 是否保留格式（粗体、斜体等）

    Returns:
        字幕文本（XML 格式）
    """
    ytt_api = YouTubeTranscriptApi()

    # 构建语言列表
    if language:
        languages = [language]
    elif not languages:
        languages = ['zh-Hans', 'zh-Hant', 'zh-CN', 'zh-TW', 'en']

    # 获取字幕列表
    transcript_list = ytt_api.list(video_id)

    # 查找匹配的字幕
    transcript = transcript_list.find_transcript(languages)

    # 获取字幕数据
    fetched_transcript = transcript.fetch(preserve_formatting=preserve_formatting)

    return fetched_transcript


def format_transcript(transcript, format_type: str = 'text') -> str:
    """
    格式化字幕输出

    Args:
        transcript: FetchedTranscript 对象
        format_type: 输出格式（text, json, srt, webvtt）

    Returns:
        格式化后的字幕字符串
    """
    formatters = {
        'text': TextFormatter(),
        'json': JSONFormatter(),
        'srt': SRTFormatter(),
        'webvtt': WebVTTFormatter(),
    }

    formatter = formatters.get(format_type.lower(), TextFormatter())
    return formatter.format_transcript(transcript)


def save_to_file(content: str, filepath: str) -> None:
    """保存内容到文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"字幕已保存到: {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description='YouTube 字幕提取工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 提取字幕（自动选择中文）
  python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID

  # 提取指定语言的字幕
  python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --lang en

  # 保存为 SRT 格式
  python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --format srt --output subtitle.srt

  # 保留格式（粗体、斜体等）
  python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --preserve-formatting
        '''
    )

    parser.add_argument(
        'url',
        help='YouTube 视频 URL 或视频 ID'
    )

    parser.add_argument(
        '--lang', '-l',
        help='字幕语言代码（如: zh-Hans, en, de, fr）'
    )

    parser.add_argument(
        '--format', '-f',
        choices=['text', 'json', 'srt', 'webvtt'],
        default='text',
        help='输出格式（默认: text）'
    )

    parser.add_argument(
        '--output', '-o',
        help='输出文件路径（如未指定则打印到控制台）'
    )

    parser.add_argument(
        '--preserve-formatting',
        action='store_true',
        help='保留字幕格式（粗体、斜体等）'
    )

    args = parser.parse_args()

    try:
        # 提取视频 ID
        print(f"正在从 URL 提取视频 ID...")
        video_id = extract_video_id(args.url)
        print(f"视频 ID: {video_id}\n")

        # 获取字幕
        print(f"正在获取字幕...")
        transcript = get_transcript(
            video_id=video_id,
            language=args.lang,
            preserve_formatting=args.preserve_formatting
        )

        # 格式化输出
        print(f"正在格式化字幕...")
        formatted_transcript = format_transcript(transcript, args.format)

        # 输出结果
        if args.output:
            save_to_file(formatted_transcript, args.output)
        else:
            print(f"\n{'='*60}")
            print(f"视频 ID: {video_id}")
            print(f"语言: {transcript.language} ({transcript.language_code})")
            print(f"字幕类型: {'自动生成' if transcript.is_generated else '人工上传'}")
            print(f"片段数量: {len(transcript)}")
            print(f"{'='*60}\n")
            print(formatted_transcript)

    except ValueError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except NoTranscriptFound as e:
        print(f"错误: 未找到字幕", file=sys.stderr)
        print(f"可用字幕信息:\n{e}", file=sys.stderr)
        sys.exit(1)
    except TranscriptsDisabled as e:
        print(f"错误: 该视频已关闭字幕功能", file=sys.stderr)
        sys.exit(1)
    except VideoUnavailable as e:
        print(f"错误: 视频不可用", file=sys.stderr)
        sys.exit(1)
    except CouldNotRetrieveTranscript as e:
        print(f"错误: 无法获取字幕\n{e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"错误: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
