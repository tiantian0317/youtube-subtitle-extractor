# 更新日志 (Changelog)

本文档记录 YouTube 字幕提取工具的所有重要更改。

## [1.0.0] - 2025-02-03

### ✨ 新功能
- 🎉 首次发布 YouTube 字幕提取工具
- 🎯 零 ASR 算力消耗，直接调用 YouTube 内部 API
- ⚡ 秒级响应，极速获取字幕
- 🌐 支持所有 YouTube 可用字幕语言
- 📝 支持多种输出格式：Text/SRT/WebVTT/JSON
- 🔄 批量处理功能，一键处理多个视频
- 🚫 无需浏览器，纯 HTTP 请求

### 📋 核心功能
- ✅ 从 YouTube URL 自动提取视频 ID
- ✅ 支持多种 URL 格式（标准 URL、短链接、移动版）
- ✅ 字幕语言优先级选择（人工上传 > 自动生成）
- ✅ 智能错误处理和友好提示
- ✅ 批量提取并生成详细日志
- ✅ Windows 控制台 UTF-8 编码支持

### 🎨 使用场景
- 🎬 视频搬运 - 获取原视频字幕
- ✂️ 视频剪辑 - 精确定位剪辑点
- 📱 自媒体创作 - 借鉴字幕内容
- 🔄 内容翻译 - 利用 YouTube 翻译功能
- 📚 资料整理 - 批量建立字幕库
- 🎓 学习笔记 - 提取教育视频字幕

### 🛠️ 技术实现
- ✅ YouTube Innertube API 集成
- ✅ XML 安全解析（defusedxml）
- ✅ 视频可播放性检测
- ✅ Cookie 同意页面处理
- ✅ IP 封禁识别和处理

### 📦 发布内容
- `youtube_subtitle_extractor.py` - 单个视频提取工具
- `batch_extract.py` - 批量提取工具
- `requirements.txt` - Python 依赖列表
- `run_test.bat` - Windows 测试脚本
- `README.md` - 完整使用文档
- `USAGE.md` - 快速使用指南
- `TEST_RESULTS.md` - 详细测试结果

### ⚠️ 已知限制
- 频繁请求可能导致 IP 被封禁
- 只能获取 YouTube 已有的字幕
- 部分视频可能存在地区或年龄限制

### 📝 TODO
- [ ] 代理池功能（多代理轮换）
- [ ] 自动重试机制
- [ ] 缓存功能
- [ ] 多线程支持
- [ ] 配置文件支持
- [ ] 进度条显示

---

## 版本说明

### 版本号格式

本项目采用 [语义化版本](https://semver.org/lang/zh-CN/)（Semantic Versioning）：

```
主版本号.次版本号.修订号 (MAJOR.MINOR.PATCH)

- MAJOR：不兼容的 API 修改
- MINOR：向下兼容的功能性新增
- PATCH：向下兼容的问题修正
```

### 更新类型

- ✨ 新功能（Added）
- 🐛 问题修正（Fixed）
- 💥 破坏性变更（Changed）
- ⚠️ 弃用警告（Deprecated）
- 🗑️ 移除（Removed）
- 🔒 安全修复（Security）

---

## 未来计划

### v1.1.0（规划中）
- 🔄 代理池功能
- 📈 性能优化
- 🎨 UI 改进

### v1.2.0（规划中）
- 📦 打包为 pip 包
- 🧪 更多测试
- 📚 更多示例

### v2.0.0（远期）
- 🚀 异步支持
- 🌐 Web 界面
- 📊 数据分析功能

---

## 反馈与建议

如有任何问题或建议，欢迎：
- 📝 提交 [Issue](https://github.com/yourusername/youtube-subtitle-extractor/issues)
- 💬 加入 QQ 群：1076150045
- 📧 发送邮件

---

## 贡献者

感谢所有贡献者的支持！

---

## 许可证

本项目采用 MIT License 开源协议。
