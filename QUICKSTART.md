# 快速开始指南

## 📦 安装

### 1. 克隆或下载项目

```bash
git clone https://github.com/yourusername/youtube-subtitle-extractor.git
cd youtube-subtitle-extractor
```

或直接下载 [Release](https://github.com/yourusername/youtube-subtitle-extractor/releases)

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install requests defusedxml
```

## 🚀 基本使用

### 单个视频提取

```bash
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --lang en
```

输出：
```
正在从 URL 提取视频 ID...

视频 ID: jNQXAC9IVRw

正在获取字幕...

============================================================
视频 ID: jNQXAC9IVRw
语言: English (en)
字幕类型: 人工上传
片段数量: 6
============================================================

All right, so here we are, in front of
elephants
the cool thing about these guys is that they
have really...
...
```

### 保存为文件

```bash
# SRT 格式（用于视频播放器）
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format srt --output video.srt

# JSON 格式（便于程序处理）
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format json --output video.json

# WebVTT 格式
python youtube_subtitle_extractor.py https://www.youtube.com/watch?v=jNQXAC9IVRw --format webvtt --output video.vtt
```

### 批量提取

```bash
# 1. 创建 URL 列表文件
echo https://www.youtube.com/watch?v=VIDEO1 > urls.txt
echo https://www.youtube.com/watch?v=VIDEO2 >> urls.txt
echo https://www.youtube.com/watch?v=VIDEO3 >> urls.txt

# 2. 运行批量提取
python batch_extract.py urls.txt --format srt --output-dir ./subtitles
```

输出：
```
YouTube 字幕批量提取工具
============================================================

开始批量提取 3 个视频的字幕...
输出目录: ./subtitles
输出格式: srt
============================================================

[1/3] 处理: https://www.youtube.com/watch?v=VIDEO1
  ✓ 成功: VIDEO1
    语言: English (en)
    类型: 人工上传
    片段数: 150

[2/3] 处理: https://www.youtube.com/watch?v=VIDEO2
  ✓ 成功: VIDEO2
    语言: Chinese (zh-Hans)
    类型: 自动生成
    片段数: 89

[3/3] 处理: https://www.youtube.com/watch?v=VIDEO3
  ✗ 未找到字幕

============================================================
批量提取完成！
成功: 2
失败: 1
总计: 3
```

## 🎯 常用场景

### 场景 1：视频搬运

```bash
# 1. 提取原视频字幕
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO_ID --format srt --output original.srt

# 2. 翻译字幕（使用翻译工具或人工翻译）
# 3. 导入到新视频（使用剪辑软件）
```

### 场景 2：内容创作参考

```bash
# 提取多个热门视频的字幕
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO1 --lang en --output ref1.txt
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO2 --lang en --output ref2.txt
python youtube_subtitle_extractor.py https://youtube.com/watch?v=VIDEO3 --lang en --output ref3.txt

# 分析字幕内容
# - 关键词提取
# - 叙事节奏分析
# - 表达方式研究
```

### 场景 3：学习资料整理

```bash
# 批量提取教育类视频字幕
python batch_extract.py education_urls.txt --format json --output-dir ./education_subs

# 后续处理
# - 建立索引数据库
# - 搜索功能
# - 学习笔记
```

## 📖 命令速查

```bash
# 显示帮助
python youtube_subtitle_extractor.py --help

# 提取指定语言
python youtube_subtitle_extractor.py URL --lang zh-Hans

# 保留格式
python youtube_subtitle_extractor.py URL --preserve-formatting

# 批量提取
python batch_extract.py urls.txt --output-dir ./subtitles

# 指定格式
python batch_extract.py urls.txt --format json --output-dir ./subs
```

## ⚠️ 注意事项

1. **语言代码**：使用正确的语言代码（zh-Hans, en, ja 等）
2. **字幕可用性**：并非所有视频都有字幕
3. **IP 限制**：频繁请求可能导致 IP 被封
4. **URL 格式**：支持完整 URL 或直接使用视频 ID

## 🆘 遇到问题？

### ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### 未找到字幕

```bash
# 检查可用语言
python youtube_subtitle_extractor.py URL --list

# 尝试不同语言
python youtube_subtitle_extractor.py URL --lang en
python youtube_subtitle_extractor.py URL --lang zh-Hans
```

### IP 被封禁

- 减少请求频率
- 等待一段时间后重试
- 使用代理（未来版本将支持）

## 💬 需要帮助？

- 📝 提交 [Issue](https://github.com/yourusername/youtube-subtitle-extractor/issues)
- 💬 加入 QQ 群：1076150045
- 📖 查看 [完整文档](README.md)
