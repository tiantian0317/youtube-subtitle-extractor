#!/usr/bin/env python3
"""
批量字幕提取示例脚本

从配置文件或命令行列表中批量提取 YouTube 视频字幕
"""

import sys
import json
from pathlib import Path

# 添加父目录到 Python 路径，以导入 youtube_transcript_api
script_dir = Path(__file__).parent
parent_dir = script_dir.parent
sys.path.insert(0, str(parent_dir))

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, SRTFormatter
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    CouldNotRetrieveTranscript,
)


def extract_video_id(url: str) -> str:
    """从 YouTube URL 中提取视频 ID"""
    import re
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|m\.youtube\.com\/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"无法从 URL 中提取视频 ID: {url}")


def get_transcript(video_id: str, language=None, preserve_formatting=False):
    """获取视频字幕"""
    ytt_api = YouTubeTranscriptApi()
    languages = [language] if language else ['zh-Hans', 'zh-Hant', 'zh-CN', 'zh-TW', 'en']
    transcript_list = ytt_api.list(video_id)
    transcript = transcript_list.find_transcript(languages)
    return transcript.fetch(preserve_formatting=preserve_formatting)


def batch_extract_from_list(urls: list, output_dir: str = './subtitles', format_type: str = 'text'):
    """
    从 URL 列表批量提取字幕

    Args:
        urls: YouTube URL 列表
        output_dir: 输出目录
        format_type: 输出格式（text/srt/json/webvtt）
    """
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 选择格式化器
    formatters = {
        'text': TextFormatter(),
        'srt': SRTFormatter(),
    }
    formatter = formatters.get(format_type, TextFormatter())

    # 文件扩展名
    ext_map = {'text': 'txt', 'srt': 'srt', 'json': 'json', 'webvtt': 'vtt'}
    ext = ext_map.get(format_type, 'txt')

    # 结果统计
    results = {
        'success': 0,
        'failed': 0,
        'errors': []
    }

    print(f"开始批量提取 {len(urls)} 个视频的字幕...")
    print(f"输出目录: {output_dir}")
    print(f"输出格式: {format_type}")
    print("=" * 60)

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] 处理: {url}")

        try:
            # 提取视频 ID
            video_id = extract_video_id(url)

            # 获取字幕
            transcript = get_transcript(video_id)

            # 格式化
            formatted = formatter.format_transcript(transcript)

            # 保存
            filepath = output_path / f"{video_id}.{ext}"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(formatted)

            print(f"  ✓ 成功: {video_id}")
            print(f"    语言: {transcript.language} ({transcript.language_code})")
            print(f"    类型: {'自动生成' if transcript.is_generated else '人工上传'}")
            print(f"    片段数: {len(transcript)}")
            results['success'] += 1

        except NoTranscriptFound as e:
            print(f"  ✗ 未找到字幕: {url}")
            results['failed'] += 1
            results['errors'].append({'url': url, 'error': 'No transcript found'})

        except TranscriptsDisabled:
            print(f"  ✗ 字幕已关闭: {url}")
            results['failed'] += 1
            results['errors'].append({'url': url, 'error': 'Transcripts disabled'})

        except VideoUnavailable:
            print(f"  ✗ 视频不可用: {url}")
            results['failed'] += 1
            results['errors'].append({'url': url, 'error': 'Video unavailable'})

        except CouldNotRetrieveTranscript as e:
            print(f"  ✗ 获取失败: {url}")
            results['failed'] += 1
            results['errors'].append({'url': url, 'error': str(e)})

        except Exception as e:
            print(f"  ✗ 未知错误: {url} - {e}")
            results['failed'] += 1
            results['errors'].append({'url': url, 'error': str(e)})

    # 打印统计
    print("\n" + "=" * 60)
    print(f"批量提取完成！")
    print(f"成功: {results['success']}")
    print(f"失败: {results['failed']}")
    print(f"总计: {len(urls)}")

    if results['errors']:
        print("\n错误详情:")
        for error in results['errors']:
            print(f"  - {error['url']}: {error['error']}")

        # 保存错误日志
        error_log = output_path / 'errors.json'
        with open(error_log, 'w', encoding='utf-8') as f:
            json.dump(results['errors'], f, ensure_ascii=False, indent=2)
        print(f"\n错误日志已保存到: {error_log}")


def batch_extract_from_file(file_path: str, output_dir: str = './subtitles', format_type: str = 'text'):
    """
    从配置文件批量提取字幕

    配置文件格式（JSON）：
    {
      "urls": [
        "https://www.youtube.com/watch?v=VIDEO_ID_1",
        "https://www.youtube.com/watch?v=VIDEO_ID_2"
      ],
      "language": "zh-Hans",  // 可选
      "format": "srt"  // 可选
    }

    或者简单文本文件（每行一个 URL）：
    https://www.youtube.com/watch?v=VIDEO_ID_1
    https://www.youtube.com/watch?v=VIDEO_ID_2
    """
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"错误: 文件不存在: {file_path}")
        return

    # 读取配置
    if file_path.suffix == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        urls = config.get('urls', [])
        format_type = config.get('format', format_type)
        # 注意：当前实现未支持从配置读取 language，需要扩展

    else:
        # 文本文件，每行一个 URL
        with open(file_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("错误: 未找到任何 URL")
        return

    batch_extract_from_list(urls, output_dir, format_type)


def main():
    import argparse
    import sys

    # 设置 Windows 控制台输出编码为 UTF-8
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

    parser = argparse.ArgumentParser(description='批量提取 YouTube 视频字幕')
    parser.add_argument('input', help='URL 列表文件或配置文件路径')
    parser.add_argument('--output-dir', '-o', default='./subtitles',
                       help='输出目录（默认: ./subtitles）')
    parser.add_argument('--format', '-f', choices=['text', 'srt', 'json', 'webvtt'],
                       default='text', help='输出格式（默认: text）')

    args = parser.parse_args()

    print("YouTube 字幕批量提取工具")
    print("=" * 60)

    # 判断是文件还是直接传入 URL
    input_path = Path(args.input)
    if input_path.exists() and input_path.is_file():
        batch_extract_from_file(str(input_path), args.output_dir, args.format)
    else:
        # 假设是逗号分隔的 URL 列表
        urls = [url.strip() for url in args.input.split(',') if url.strip()]
        batch_extract_from_list(urls, args.output_dir, args.format)


if __name__ == '__main__':
    main()
