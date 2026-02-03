# 贡献指南

感谢您对 YouTube 字幕提取工具感兴趣！我们欢迎任何形式的贡献。

## 🤝 如何贡献

### 报告 Bug

如果您发现了 Bug，请：

1. 检查 [Issues](https://github.com/yourusername/youtube-subtitle-extractor/issues) 看是否已有相同问题
2. 如果没有，创建一个新的 [Bug 报告](https://github.com/yourusername/youtube-subtitle-extractor/issues/new?template=bug_report.md)
3. 提供详细的复现步骤和环境信息

### 提出新功能

如果您有新功能的想法：

1. 检查 [Issues](https://github.com/yourusername/youtube-subtitle-extractor/issues) 看是否已有相同请求
2. 如果没有，创建一个新的 [功能请求](https://github.com/yourusername/youtube-subtitle-extractor/issues/new?template=feature_request.md)
3. 详细描述您的想法和使用场景

### 提交代码

#### 开发流程

1. **Fork 仓库**

   点击 GitHub 页面右上角的 "Fork" 按钮

2. **克隆您的 Fork**

   ```bash
   git clone https://github.com/YOUR_USERNAME/youtube-subtitle-extractor.git
   cd youtube-subtitle-extractor
   ```

3. **创建新分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **进行更改**

   - 遵循项目的代码风格
   - 添加必要的测试
   - 更新相关文档

5. **提交更改**

   ```bash
   git add .
   git commit -m "Add some feature"
   ```

   提交信息格式：
   ```
   <type>: <subject>

   <body>
   ```

   Type 可以是：
   - `feat`: 新功能
   - `fix`: Bug 修复
   - `docs`: 文档更新
   - `style`: 代码格式（不影响代码运行）
   - `refactor`: 重构
   - `perf`: 性能优化
   - `test`: 测试相关
   - `chore`: 构建或辅助工具的变动

6. **推送到您的 Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**

   访问原仓库并点击 "New Pull Request"

#### PR 检查清单

- [ ] 代码符合项目的代码风格
- [ ] 已添加必要的测试
- [ ] 所有测试通过
- [ ] 已更新相关文档
- [ ] PR 描述清晰说明了更改

## 📋 代码规范

### Python 代码风格

- 遵循 PEP 8 规范
- 使用有意义的变量和函数名
- 添加必要的注释和文档字符串
- 最大行长度：127 字符

### Git 提交信息

使用清晰的提交信息：

```
feat: 添加代理池功能

- 支持多代理轮换
- 添加代理配置文件
- 更新文档
```

## 🧪 测试

### 运行测试

```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest tests/test_extractor.py

# 查看覆盖率
python -m pytest --cov=.
```

### 添加新测试

1. 在 `tests/` 目录创建测试文件
2. 编写测试用例
3. 确保测试通过

## 📚 文档

### 更新文档

当添加新功能或修改现有功能时，请更新：

- `README.md` - 主要功能和使用方法
- `CHANGELOG.md` - 更新日志
- `USAGE.md` - 使用指南
- 代码注释和文档字符串

### 文档语言

- 主要使用中文编写
- 重要的用户界面文本可以提供英文翻译

## 🌟 特别关注的功能

我们特别欢迎以下方面的贡献：

- 🔄 **代理池功能** - 多代理轮换，避免 IP 封禁
- ⚡ **性能优化** - 加速批量处理
- 🧪 **测试覆盖** - 提高代码质量
- 📚 **文档改进** - 让工具更易用
- 🌍 **多语言支持** - 界面和错误提示

## 💬 交流

- 💬 QQ 群：1076150045
- 📝 GitHub Issues
- 📧 邮件

## 📄 许可证

通过提交您的 Pull Request，您同意您的贡献将在 MIT License 下发布。

## 🙏 致谢

感谢所有贡献者！您的贡献让这个工具变得更好。

---

有任何问题？请随时联系我们！
