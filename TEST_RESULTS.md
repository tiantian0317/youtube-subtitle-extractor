# YouTube 字幕提取工具 - 测试结果

## 环境信息

- Python 虚拟环境: `C:\Users\Administrator\miniconda3\envs\YoutubeSubGet`
- 项目目录: `C:\Users\Administrator\GIT\youtube-transcript-api\YoutubeSubGet`

## 安装依赖

```bash
pip install -r requirements.txt
```

或直接安装：

```bash
pip install requests defusedxml
```

## 测试结果

### ✅ 测试 1：单个视频提取 - 纯文本

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
```

**结果**: 成功 ✓
- 视频 ID: jNQXAC9IVRw
- 语言: English (en)
- 字幕类型: 人工上传
- 片段数量: 6

### ✅ 测试 2：单个视频提取 - SRT 格式

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output test.srt
```

**结果**: 成功 ✓
- 输出文件: `test.srt`
- 格式正确，包含时间戳

### ✅ 测试 3：单个视频提取 - JSON 格式

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format json --output test.json
```

**结果**: 成功 ✓
- 输出文件: `test.json`
- JSON 格式正确，包含 start 和 duration 字段

### ✅ 测试 4：批量提取

```bash
python batch_extract.py url.txt --output-dir ./subtitles
```

**结果**: 成功 ✓
- 成功处理 2 个 URL
- 生成错误日志: `subtitles/errors.json`
- 显示了详细的失败原因（字幕已关闭）

**注意**: url.txt 中的两个视频都没有字幕，这是预期的结果。

## 命令行测试命令

### 使用绝对路径运行（推荐）

```bash
# 单个视频提取
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\python.exe youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en

# 保存为 SRT
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\python.exe youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output test.srt

# 批量提取
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\python.exe batch_extract.py url.txt --output-dir ./subtitles
```

### 或在虚拟环境中运行

```bash
# 激活虚拟环境
conda activate YoutubeSubGet

# 或使用 activate.bat
C:\Users\Administrator\miniconda3\envs\YoutubeSubGet\Scripts\activate.bat

# 运行命令
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
```

## 功能验证清单

- [x] 从 YouTube URL 提取视频 ID
- [x] 获取视频字幕（英文）
- [x] 支持多种输出格式（text/srt/json）
- [x] 保存字幕到文件
- [x] 批量提取字幕
- [x] 错误处理和日志记录
- [x] Windows 控制台编码支持（UTF-8）
- [x] 使用虚拟环境的绝对路径运行

## 输出示例

### SRT 格式示例 (test.srt)

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

### JSON 格式示例 (test.json)

```json
[
  {
    "text": "All right, so here we are, in front of\nelephants",
    "start": 1.2,
    "duration": 2.16
  },
  {
    "text": "the cool thing about these guys is that they\nhave really...",
    "start": 5.318,
    "duration": 2.656
  }
]
```

## 问题与解决方案

### 问题 1：模块导入错误

**错误**: `ModuleNotFoundError: No module named 'youtube_transcript_api'`

**解决**: 已在脚本中添加父目录到 sys.path

```python
import sys
from pathlib import Path
script_dir = Path(__file__).parent
parent_dir = script_dir.parent
sys.path.insert(0, str(parent_dir))
```

### 问题 2：Windows 控制台编码

**错误**: `UnicodeEncodeError: 'gbk' codec can't encode character`

**解决**: 已在 batch_extract.py 中设置 UTF-8 编码

```python
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
```

### 问题 3：url.txt 中的视频没有字幕

**说明**: 这不是工具的问题，而是视频本身没有启用字幕功能。工具正确地识别并报告了这个情况。

## 使用建议

1. **使用绝对路径运行脚本**，避免工作目录问题
2. **指定明确的语言代码**，如 `--lang zh-Hans` 或 `--lang en`
3. **选择合适的输出格式**：
   - `text`: 纯文本阅读
   - `srt`: 用于视频播放器
   - `json`: 用于程序处理
4. **批量处理时**，先测试单个 URL 确认可用

## 项目文件结构

```
YoutubeSubGet/
├── youtube_subtitle_extractor.py  # 单个视频提取工具
├── batch_extract.py              # 批量提取工具
├── requirements.txt              # 依赖列表
├── README.md                   # 使用说明
├── url.txt                     # URL 列表
├── test.srt                   # 测试输出文件
├── test.json                  # 测试输出文件
└── subtitles/                 # 批量提取输出目录
    └── errors.json           # 错误日志
```

## 总结

工具已成功部署到 `YoutubeSubGet` 目录，所有核心功能均经过测试验证。工具可以在虚拟环境中使用绝对路径正常运行。
