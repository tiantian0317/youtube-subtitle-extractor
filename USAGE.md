# YouTube 字幕提取工具 - 使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试脚本（Windows）

双击运行 `run_test.bat`，或在命令行中执行：

```bash
run_test.bat
```

## 手动运行

### 方法 1：使用绝对路径（推荐）

```bash
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\python.exe youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID
```

### 方法 2：激活虚拟环境后运行

```bash
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\Scripts\activate.bat
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID
```

## 使用示例

### 提取单个视频（纯文本）

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
```

### 提取单个视频（SRT 格式）

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output video.srt
```

### 提取单个视频（JSON 格式）

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format json --output video.json
```

### 批量提取

```bash
python batch_extract.py url.txt --output-dir ./subtitles
```

### 指定中文字幕

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --lang zh-Hans
```

## 参数说明

### youtube_subtitle_extractor.py

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `url` | - | YouTube URL 或视频 ID（必需） | `https://www.youtube.com/watch?v=xxx` |
| `--lang` | `-l` | 字幕语言代码 | `--lang zh-Hans` |
| `--format` | `-f` | 输出格式 | `--format srt` |
| `--output` | `-o` | 输出文件路径 | `--output video.srt` |

### batch_extract.py

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `input` | - | URL 列表文件 | `url.txt` |
| `--output-dir` | `-o` | 输出目录 | `--output-dir ./subtitles` |
| `--format` | `-f` | 输出格式 | `--format srt` |

## 常用语言代码

| 语言 | 代码 |
|------|------|
| 简体中文 | `zh-Hans` |
| 繁体中文 | `zh-Hant` |
| 英语 | `en` |
| 日语 | `ja` |
| 韩语 | `ko` |
| 德语 | `de` |
| 法语 | `fr` |
| 西班牙语 | `es` |

## 输出格式

### Text（纯文本）
```
All right, so here we are, in front of
elephants
the cool thing about these guys is that they
have really...
```

### SRT（字幕文件）
```
1
00:00:01,200 --> 00:00:03,360
All right, so here we are, in front of
elephants

2
00:00:05,318 --> 00:00:07,974
the cool thing about these guys is that they
have really...
```

### JSON（结构化数据）
```json
[
  {
    "text": "All right, so here we are, in front of\nelephants",
    "start": 1.2,
    "duration": 2.16
  }
]
```

## 故障排除

### 问题：ModuleNotFoundError

**解决**：安装依赖
```bash
pip install requests defusedxml
```

### 问题：找不到字幕

**解决**：
1. 确认视频有字幕
2. 尝试不同的语言代码
3. 使用 `--lang` 参数明确指定语言

### 问题：Windows 控制台乱码

**解决**：使用 run_test.bat（已设置 UTF-8 编码）

### 问题：IP 被封禁

**解决**：
- 减少请求频率
- 等待一段时间后重试
- 使用代理（需要修改代码）

## 文件说明

| 文件 | 说明 |
|------|------|
| `youtube_subtitle_extractor.py` | 单个视频提取工具 |
| `batch_extract.py` | 批量提取工具 |
| `requirements.txt` | Python 依赖列表 |
| `run_test.bat` | Windows 测试脚本 |
| `url.txt` | URL 列表文件 |
| `README.md` | 详细文档 |
| `USAGE.md` | 本文件 |
| `TEST_RESULTS.md` | 测试结果 |

## 更多信息

详细测试结果请查看：`TEST_RESULTS.md`
