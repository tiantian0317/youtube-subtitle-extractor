<div align="center">

# YouTube 字幕提取工具

**零 ASR 算力消耗 · 直接获取字幕 · 视频创作必备工具**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/yourusername/youtube-subtitle-extractor)

[English](#english) | [简体中文](#简体中文)

---

### ✨ 特性

- 🎯 **零 ASR 算力** - 直接调用 YouTube 内部 API，无需本地 ASR 处理
- ⚡ **极速获取** - 秒级响应，支持批量处理
- 🌐 **多语言支持** - 支持所有 YouTube 可用字幕语言
- 📝 **多种格式** - 输出 Text/SRT/WebVTT/JSON 格式
- 🔄 **批量处理** - 一键处理多个视频字幕
- 🚫 **无浏览器** - 纯 HTTP 请求，无需 Selenium 等工具
- 📊 **结构化数据** - 包含时间戳和持续时间信息

---

### 🎯 适用场景

完美适用于：

| 场景 | 说明 |
|------|------|
| 🎬 **视频搬运** | 获取原视频字幕，快速搬运到其他平台 |
| ✂️ **视频剪辑** | 提取字幕用于精确定位剪辑点 |
| 📱 **自媒体创作** | 借鉴字幕内容，启发创作灵感 |
| 🔄 **内容翻译** | 利用 YouTube 翻译功能，获取多语言字幕 |
| 📚 **资料整理** | 批量下载字幕，建立字幕库 |
| 🎓 **学习笔记** | 提取教育类视频字幕，方便复习 |

---

### 🚀 快速开始

#### 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install requests defusedxml
```

#### 基本使用

**单个视频提取：**

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
```

**保存为 SRT 字幕文件：**

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output video.srt
```

**批量提取：**

```bash
python batch_extract.py url.txt --output-dir ./subtitles
```

---

### 📖 详细使用

#### 1. 提取单个视频

```bash
# 纯文本格式
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --lang zh-Hans

# SRT 字幕格式（用于视频播放器）
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --format srt --output video.srt

# JSON 格式（便于程序处理）
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --format json --output video.json

# WebVTT 格式
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=VIDEO_ID --format webvtt --output video.vtt
```

#### 2. 批量处理

创建 `url.txt` 文件：

```text
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
```

运行批量提取：

```bash
python batch_extract.py url.txt --format srt --output-dir ./subtitles
```

#### 3. 命令行参数

**youtube_subtitle_extractor.py：**

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `url` | - | YouTube URL 或视频 ID（必需） | `https://youtube.com/watch?v=xxx` |
| `--lang` | `-l` | 字幕语言代码 | `--lang zh-Hans` |
| `--format` | `-f` | 输出格式 | `--format srt` |
| `--output` | `-o` | 输出文件路径 | `--output video.srt` |
| `--preserve-formatting` | - | 保留字幕格式 | `--preserve-formatting` |

**batch_extract.py：**

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `input` | - | URL 列表文件 | `url.txt` |
| `--output-dir` | `-o` | 输出目录 | `--output-dir ./subtitles` |
| `--format` | `-f` | 输出格式 | `--format srt` |

#### 4. 常用语言代码

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
| 俄语 | `ru` |
| 阿拉伯语 | `ar` |

---

### 🏗️ 设计原理

#### 核心设计思想

**为什么不需要 ASR 算力？**

本工具采用"**API 调用**模式，而非"**本地处理**"模式：

```
传统 ASR 方式：
视频 → 本地 ASR 引擎 → 字幕文本
      ↓
  需要大量算力（CPU/GPU）
  处理时间长
  准确率依赖模型

本工具方式：
视频 → YouTube 内部 API → 字幕数据
      ↓
  零算力消耗
  秒级响应
  直接获取官方字幕
```

#### 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                  YouTube 字幕提取工具                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ├─► 单个视频提取器
                            │   └─ youtube_subtitle_extractor.py
                            │
                            ├─► 批量提取器
                            │   └─ batch_extract.py
                            │
                            └─► 格式化器
                                ├─ TextFormatter
                                ├─ SRTFormatter
                                ├─ WebVTTFormatter
                                └─ JSONFormatter
                            │
                            └─► 核心 API 客户端
                                └─ YouTube Innertube API
```

#### 数据流

```
1. 输入 YouTube URL
   ↓
2. 提取视频 ID
   ↓
3. 调用 YouTube Innertube API
   └─ POST https://www.youtube.com/youtubei/v1/player
      └─ 获取 captions JSON
   ↓
4. 下载字幕 XML 文件
   ↓
5. 解析并格式化输出
   ↓
6. 保存到文件或打印到控制台
```

---

### 🧠 核心算法

#### 1. 视频 ID 提取算法

```python
def extract_video_id(url: str) -> str:
    """从 YouTube URL 提取视频 ID"""
    
    # 支持多种 URL 格式
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|m\.youtube\.com\/watch\?v=)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',  # 直接输入 video ID
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    raise ValueError(f"无法从 URL 中提取视频 ID: {url}")
```

**支持的 URL 格式：**
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`
- 直接输入 `VIDEO_ID`

#### 2. YouTube Innertube API 调用

```python
def fetch_captions_json(video_id: str) -> Dict:
    """调用 YouTube Innertube API 获取字幕信息"""
    
    # 1. 提取 API Key
    html = fetch_video_html(video_id)
    api_key = extract_innertube_api_key(html)
    
    # 2. 调用 API
    response = requests.post(
        "https://www.youtube.com/youtubei/v1/player?key={api_key}",
        json={
            "context": {
                "client": {
                    "clientName": "ANDROID",
                    "clientVersion": "20.10.38"
                }
            },
            "videoId": video_id
        }
    )
    
    # 3. 提取字幕信息
    return response.json()["captions"]["playerCaptionsTracklistRenderer"]
```

**关键点：**
- 使用 Android 客户端模拟，避免复杂的 Web 端逻辑
- 官方 API 响应，数据准确可靠
- 无需浏览器，纯 HTTP 请求

#### 3. 字幕语言优先级算法

```python
def find_transcript(language_codes: List[str]) -> Transcript:
    """按优先级查找字幕"""
    
    # 语言优先级队列
    for language_code in language_codes:
        # 字幕类型优先级：人工上传 > 自动生成
        for transcript_dict in [manually_created, generated]:
            if language_code in transcript_dict:
                return transcript_dict[language_code]
    
    raise NoTranscriptFound(language_codes)
```

**算法优势：**
- ✅ 优先选择人工上传字幕（更准确）
- ✅ 回退到自动生成字幕（覆盖更广）
- ✅ 支持多语言备选

#### 4. XML 解析算法

```python
def parse_transcript_xml(xml_text: str) -> List[Subtitle]:
    """解析 YouTube 字幕 XML"""
    
    subtitles = []
    for element in ElementTree.fromstring(xml_text):
        subtitle = {
            "text": unescape(element.text),  # HTML 实体解码
            "start": float(element.attrib["start"]),  # 开始时间（秒）
            "duration": float(element.attrib.get("dur", "0.0"))  # 持续时间（秒）
        }
        subtitles.append(subtitle)
    
    return subtitles
```

**数据结构：**
```json
[
  {
    "text": "Hello World",
    "start": 1.5,
    "duration": 2.3
  }
]
```

---

### 📊 输出格式

#### 1. Text（纯文本）

```
All right, so here we are, in front of
elephants
the cool thing about these guys is that they
have really...
```

**用途：** 快速阅读、内容分析

#### 2. SRT（SubRip 字幕）

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

**用途：** 视频播放器、剪辑软件

#### 3. WebVTT（Web 视频文本轨道）

```
WEBVTT

00:00:01.200 --> 00:00:03.360
All right, so here we are, in front of
elephants

00:00:05.318 --> 00:00:07.974
the cool thing about these guys is that they
have really...
```

**用途：** Web 播放器、HTML5 视频

#### 4. JSON（结构化数据）

```json
[
  {
    "text": "All right, so here we are, in front of\nelephants",
    "start": 1.2,
    "duration": 2.16
  }
]
```

**用途：** 程序处理、数据分析

---

### ⚠️ 局限性

本工具依赖 YouTube 内部 API，存在以下局限性：

| 局限性 | 说明 | 影响程度 |
|---------|------|-----------|
| 🚫 **IP 限制** | 频繁请求可能导致 IP 被封禁 | ⚠️ 中等 |
| 🚫 **字幕依赖** | 只能获取 YouTube 已有的字幕 | ⚠️ 中等 |
| 🚫 **API 变更** | YouTube 可能随时更改 API | ⚠️ 高 |
| 🚫 **私有视频** | 无法获取私人视频字幕 | ⚠️ 低 |
| 🚫 **年龄限制** | 某些年龄限制视频可能需要认证 | ⚠️ 中等 |
| 🚫 **地区限制** | 部分视频存在地区访问限制 | ⚠️ 低 |

### 解决方案

#### 1. IP 封禁问题

**TODO：** 增加代理池功能

当前解决方案：
- 控制请求频率
- 使用轮换住宅代理
- 添加请求间隔

未来实现：
```python
# 代理池配置（TODO）
PROXY_POOL = {
    "type": "rotating",  # 轮换代理
    "providers": ["webshare", "luminati", "smartproxy"],
    "pool_size": 100,
    "retry_on_429": True
}
```

#### 2. 字幕可用性

**最佳实践：**
- 先检查字幕列表：`python youtube_subtitle_extractor.py VIDEO_ID --list`
- 使用多个语言代码备选：`--lang zh-Hans,en,ja`
- 优先选择人工上传字幕

#### 3. API 变更应对

**策略：**
- 监控 YouTube API 变更
- 快速响应和修复
- 版本化 API 端点

---

### 🎁 使用案例

#### 案例 1：视频搬运

**场景：** 从 YouTube 搬运视频到 Bilibili/抖音

```bash
# 1. 提取原视频字幕
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO_ID --format srt --output original.srt

# 2. 使用翻译工具翻译字幕
#（或其他翻译工具）

# 3. 导入到新视频
#（使用剪辑软件导入翻译后的字幕）
```

#### 案例 2：批量整理字幕库

**场景：** 收集教育类视频字幕，建立学习资料库

```bash
# 1. 创建视频列表
cat > tutorial_urls.txt <<EOF
https://youtube.com/watch?v=VIDEO1
https://youtube.com/watch?v=VIDEO2
https://youtube.com/watch?v=VIDEO3
EOF

# 2. 批量提取
python batch_extract.py tutorial_urls.txt --format json --output-dir ./tutorial_library

# 3. 后续处理
# - 建立索引数据库
# - 内容分析
# - 搜索功能
```

#### 案例 3：内容创作参考

**场景：** 借鉴热门视频的叙事结构和表达方式

```bash
# 1. 提取多个视频的字幕
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO1 --lang en --output ref1.txt
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO2 --lang en --output ref2.txt

# 2. 分析文本
# - 关键词提取
# - 叙事节奏分析
# - 表达方式研究
```

---

### 📈 性能对比

| 方案 | 算力需求 | 处理时间 | 准确率 | 成本 |
|------|-----------|---------|--------|------|
| **本工具** | ❌ 零算力 | ⚡ 秒级 | ✅ 官方质量 | 💰 免费 |
| 本地 ASR | 🔥 高算力 | ⏱️ 分钟级 | ⚠️ 依赖模型 | 💸 昂贵 |
| 云端 ASR | ❌ 本地零算力 | ⚡ 秒级 | ⚠️ 依赖模型 | 💸 按量付费 |

**结论：** 本工具在成本和效率上具有绝对优势。

---

### 🛠️ 技术栈

- **Python 3.8+**
- **requests** - HTTP 客户端
- **defusedxml** - 安全的 XML 解析
- **argparse** - 命令行参数解析

---

### 📝 TODO

- [ ] **代理池功能** - 支持多代理轮换，避免 IP 封禁
- [ ] **自动重试机制** - 429 错误自动重试
- [ ] **缓存功能** - 缓存已获取的字幕，避免重复请求
- [ ] **多线程支持** - 加速批量处理
- [ ] **配置文件** - 支持更灵活的配置方式
- [ ] **进度条** - 批量处理时显示进度

---

### 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

---

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

### 💡 支持与交流

> 💡 **自媒体全家桶用户群：1076150045** - 欢迎加入交流！

加入群组，您可以：
- 🎓 获取工具使用教程
- 💬 与其他创作者交流经验
- 🆕 获取最新功能更新
- 🐛 报告问题并获得帮助
- 🎁 参与内测新功能

---

### 🌟 Star History

如果这个工具对你有帮助，请给个 Star ⭐

---

<div align="center">

### 📢 免责声明

本工具仅供学习和研究使用，请遵守 YouTube 服务条款和相关法律法规。使用者应自行承担使用本工具产生的风险和法律责任。

Made with ❤️ by AI Tools Team

</div>

---

<div align="center">

---

### English

**YouTube Subtitle Extractor - Zero ASR Computation**

A powerful tool to extract YouTube video subtitles without any ASR computation.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/yourusername/youtube-subtitle-extractor)

---

### ✨ Features

- 🎯 **Zero ASR** - Direct API calls, no local processing needed
- ⚡ **Lightning Fast** - Get subtitles in seconds
- 🌐 **Multi-language** - Supports all YouTube subtitle languages
- 📝 **Multiple Formats** - Text/SRT/WebVTT/JSON
- 🔄 **Batch Processing** - Process multiple videos at once
- 🚫 **No Browser** - Pure HTTP requests

---

### 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Extract single video
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en

# Save as SRT
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output video.srt

# Batch extract
python batch_extract.py url.txt --output-dir ./subtitles
```

---

### 🏗️ Design Philosophy

**Why Zero ASR?**

This tool uses an "API Calling" model instead of "Local Processing":

```
Traditional ASR:
Video → Local ASR Engine → Subtitles
      ↓
  High CPU/GPU usage
  Slow processing
  Accuracy depends on model

This Tool:
Video → YouTube Internal API → Subtitles
      ↓
  Zero computation
  Instant response
  Official quality
```

---

### 🧠 Core Algorithms

1. **Video ID Extraction** - Supports multiple URL formats
2. **YouTube Innertube API** - Direct API calls
3. **Language Priority** - Manual > Auto-generated
4. **XML Parsing** - Secure and fast

---

### ⚠️ Limitations

| Limitation | Impact |
|------------|---------|
| 🚫 **IP Blocking** | ⚠️ Medium |
| 🚫 **Subtitle Dependency** | ⚠️ Medium |
| 🚫 **API Changes** | ⚠️ High |
| 🚫 **Private Videos** | ⚠️ Low |

---

### 📝 TODO

- [ ] **Proxy Pool** - Multi-proxy rotation
- [ ] **Auto Retry** - Automatic retry on 429
- [ ] **Caching** - Cache retrieved subtitles
- [ ] **Multi-threading** - Faster batch processing
- [ ] **Config File** - More flexible configuration
- [ ] **Progress Bar** - Show progress during batch processing

---

### 💡 Support & Community

> 💡 **Join our community: QQ Group 1076150045** - Share and learn!

---

<div align="center">

**Made with ❤️ by AI Tools Team**

</div>

</div>
