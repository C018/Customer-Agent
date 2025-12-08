# 文档索引 (Documentation Index)

本文档提供了拼多多智能客服系统所有文档的索引和概览。

## 📚 文档列表

### 核心文档

#### 1. [README.md](../README.md)
- **简介**: 项目主页和快速入门指南
- **内容**:
  - 项目简介和功能特性
  - 快速开始步骤
  - 项目结构说明
  - 使用指南
  - 联系方式
- **适用人群**: 所有用户

#### 2. [安装指南 (INSTALLATION_GUIDE.md)](./INSTALLATION_GUIDE.md) 🔥
- **简介**: 详细的安装步骤和说明
- **内容**:
  - 前提条件检查
  - 三种安装方式（uv、pip、开发模式）
  - 不同操作系统的安装说明
  - 验证安装的方法
  - 常见安装问题解决
- **适用人群**: 首次安装的用户
- **推荐指数**: ⭐⭐⭐⭐⭐

### 依赖相关文档

#### 3. [依赖分析文档 (DEPENDENCY_ANALYSIS.md)](./DEPENDENCY_ANALYSIS.md) 🔥
- **简介**: 完整的依赖项分析和说明
- **内容**:
  - 所有依赖的详细说明
  - 每个依赖的用途和使用位置
  - 依赖关系图
  - 依赖冲突分析
  - 系统资源要求
  - 依赖更新策略
- **适用人群**: 
  - 想深入了解项目依赖的用户
  - 遇到依赖问题的用户
  - 开发者
- **推荐指数**: ⭐⭐⭐⭐⭐

#### 4. [依赖问题快速修复指南 (DEPENDENCY_QUICK_FIX.md)](./DEPENDENCY_QUICK_FIX.md) 🚑
- **简介**: 常见依赖问题的快速解决方案
- **内容**:
  - 快速诊断步骤
  - 10+ 常见错误及解决方案
  - 完全重新安装指南
  - 预防性维护建议
- **适用人群**: 遇到依赖错误的用户
- **推荐指数**: ⭐⭐⭐⭐⭐
- **特点**: 简洁明了，直接给出解决方案

### 配置文档

#### 5. [AI Bot 配置指南 (AI_BOT_CONFIG.md)](./AI_BOT_CONFIG.md)
- **简介**: AI 服务配置详细说明
- **内容**:
  - Coze AI 配置
  - OpenAI 配置
  - Azure OpenAI 配置
  - 配置文件格式说明
- **适用人群**: 需要配置 AI 服务的用户
- **推荐指数**: ⭐⭐⭐⭐

#### 6. [更新日志 (CHANGES_SUMMARY.md)](./CHANGES_SUMMARY.md)
- **简介**: 项目更新和变更记录
- **内容**: 版本更新内容和重要变更
- **适用人群**: 想了解项目历史的用户

### 技术文件

#### 7. [pyproject.toml](../pyproject.toml)
- **简介**: Python 项目配置文件
- **内容**: 项目元信息和依赖声明
- **适用人群**: 开发者

#### 8. [requirements.txt](../requirements.txt)
- **简介**: pip 格式的依赖列表（自动生成）
- **内容**: 所有依赖及其精确版本
- **适用人群**: 使用 pip 的用户

#### 9. [uv.lock](../uv.lock)
- **简介**: uv 锁定文件
- **内容**: 依赖的精确版本锁定
- **适用人群**: 使用 uv 的用户

## 🚦 使用场景导航

### 场景 1: 我是新用户，想快速开始

**推荐阅读顺序**:
1. [README.md](../README.md) - 了解项目
2. [安装指南 (INSTALLATION_GUIDE.md)](./INSTALLATION_GUIDE.md) - 安装系统
3. [AI Bot 配置指南 (AI_BOT_CONFIG.md)](./AI_BOT_CONFIG.md) - 配置 AI 服务

### 场景 2: 安装过程中遇到错误

**推荐阅读顺序**:
1. [依赖问题快速修复指南 (DEPENDENCY_QUICK_FIX.md)](./DEPENDENCY_QUICK_FIX.md) - 快速查找解决方案
2. 如果问题未解决，查看 [依赖分析文档 (DEPENDENCY_ANALYSIS.md)](./DEPENDENCY_ANALYSIS.md) - 深入了解依赖
3. 如果仍未解决，查看 [安装指南](./INSTALLATION_GUIDE.md) 的常见问题部分

### 场景 3: 我想了解项目使用了哪些技术

**推荐阅读**:
1. [README.md](../README.md) - 技术架构部分
2. [依赖分析文档 (DEPENDENCY_ANALYSIS.md)](./DEPENDENCY_ANALYSIS.md) - 详细的依赖说明

### 场景 4: 我是开发者，想参与贡献

**推荐阅读顺序**:
1. [README.md](../README.md) - 项目结构和贡献指南
2. [安装指南 (INSTALLATION_GUIDE.md)](./INSTALLATION_GUIDE.md) - 开发环境安装
3. [依赖分析文档 (DEPENDENCY_ANALYSIS.md)](./DEPENDENCY_ANALYSIS.md) - 依赖详解
4. 查看源代码和注释

### 场景 5: 系统运行出现问题

**推荐步骤**:
1. 查看 `logs` 目录下的日志文件
2. 根据错误类型：
   - 依赖相关 → [依赖问题快速修复指南](./DEPENDENCY_QUICK_FIX.md)
   - AI 服务相关 → [AI Bot 配置指南](./AI_BOT_CONFIG.md)
   - 其他问题 → 在 GitHub Issues 中搜索或提问

## 📝 文档更新记录

| 文档 | 最后更新 | 版本 | 说明 |
|------|---------|------|------|
| DEPENDENCY_ANALYSIS.md | 2025-12-08 | 1.0.0 | 新增依赖分析文档 |
| DEPENDENCY_QUICK_FIX.md | 2025-12-08 | 1.0.0 | 新增快速修复指南 |
| INSTALLATION_GUIDE.md | 2025-12-08 | 1.0.0 | 新增安装指南 |
| README.md | 2025-12-08 | 1.0.0 | 添加文档链接 |
| AI_BOT_CONFIG.md | - | - | 已存在 |
| CHANGES_SUMMARY.md | - | - | 已存在 |

## 🆘 获取帮助

如果文档中的信息无法解决你的问题：

1. **搜索已有问题**: 
   - 访问 [GitHub Issues](https://github.com/C018/Customer-Agent/issues)
   - 使用关键词搜索是否有类似问题

2. **提交新问题**:
   - 描述遇到的问题
   - 提供以下信息:
     - Python 版本
     - 操作系统版本
     - 错误信息截图
     - 相关日志
   - 说明已尝试的解决方案

3. **加入社区**:
   - 扫描 README 中的频道二维码
   - 与其他用户交流

## 💡 建议

- **首次安装**: 务必完整阅读安装指南，可以避免大多数问题
- **遇到问题**: 先查看快速修复指南，通常能快速解决
- **深入学习**: 阅读依赖分析文档，了解系统架构
- **保持更新**: 定期查看更新日志，了解新功能和修复

## 📖 文档贡献

如果你发现文档中的错误或有改进建议：

1. Fork 项目
2. 修改文档
3. 提交 Pull Request
4. 说明修改内容和原因

我们欢迎所有形式的文档改进！

---

**最后更新**: 2025-12-08  
**维护者**: [JC0v0](https://github.com/JC0v0)
