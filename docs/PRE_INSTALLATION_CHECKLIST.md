# 安装前检查清单 (Pre-Installation Checklist)

在开始安装拼多多智能客服系统之前，请使用此清单确保您的环境满足所有要求。这可以帮助您避免大多数常见的安装问题。

## ✅ 系统要求检查

### 1. 操作系统
- [ ] Windows 10/11（推荐）
- [ ] macOS 10.15 或更高版本
- [ ] Linux (Ubuntu 20.04+ / Fedora 30+ / 其他现代发行版)

**验证命令**:
```bash
# Windows
winver

# macOS
sw_vers

# Linux
lsb_release -a
```

### 2. Python 版本
- [ ] Python 3.11 或更高版本已安装
- [ ] `python --version` 显示正确版本
- [ ] Python 已添加到系统 PATH

**验证命令**:
```bash
python --version
# 或
python3 --version
```

**期望输出**: `Python 3.11.x` 或更高

### 3. pip 包管理器
- [ ] pip 已安装
- [ ] pip 版本为最新

**验证命令**:
```bash
python -m pip --version
```

**更新 pip**:
```bash
python -m pip install --upgrade pip
```

## 💾 磁盘空间检查

### 所需空间
- [ ] 至少 2GB 可用磁盘空间（最低）
- [ ] 推荐 5GB 或更多（包括浏览器和日志）

**空间分配**:
- Python 依赖包: ~500MB
- Chrome 浏览器: ~300MB
- 数据库和配置: ~50MB
- 日志文件: ~100MB (随时间增长)
- 临时文件: ~500MB
- 预留空间: ~1GB

**验证命令**:
```bash
# Windows
dir C:\

# macOS/Linux
df -h ~
```

## 🌐 网络连接检查

### 1. 基本连接
- [ ] 可以访问互联网
- [ ] 可以访问 pypi.org
- [ ] 可以访问 GitHub

**验证命令**:
```bash
# 测试 PyPI 连接
curl -I https://pypi.org/simple/

# 测试 GitHub 连接
curl -I https://github.com
```

### 2. 特定服务访问
根据您计划使用的 AI 服务，确保可以访问：
- [ ] Coze API (api.coze.com / api.coze.cn)
- [ ] OpenAI API (api.openai.com)
- [ ] Azure OpenAI (您的 Azure endpoint)
- [ ] 拼多多商家平台 (mms.pinduoduo.com)

### 3. 防火墙和代理
- [ ] 防火墙允许 Python 访问网络
- [ ] 如需代理，已正确配置代理设置
- [ ] WebSocket 连接未被阻止

## 🔧 系统依赖检查

### Windows 用户
- [ ] Visual C++ Redistributable 已安装
  - 下载: https://aka.ms/vs/17/release/vc_redist.x64.exe
- [ ] .NET Framework 4.8 或更高（通常已预装）

**验证**: 运行示例 PyQt6 程序，如果报 DLL 错误则需要安装

### macOS 用户
- [ ] Xcode Command Line Tools 已安装

**安装命令**:
```bash
xcode-select --install
```

### Linux 用户 (Ubuntu/Debian)
- [ ] 必需的系统库已安装

**安装命令**:
```bash
sudo apt update
sudo apt install -y \
    python3.11-dev \
    build-essential \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libxkbcommon-x11-0 \
    libdbus-1-3 \
    libgl1-mesa-glx \
    libegl1-mesa \
    libfontconfig1 \
    libglib2.0-0
```

### Linux 用户 (Fedora/RHEL)
- [ ] 必需的系统库已安装

**安装命令**:
```bash
sudo dnf install -y \
    python3.11-devel \
    gcc \
    gcc-c++ \
    xcb-util-cursor \
    libxkbcommon-x11 \
    dbus-libs \
    mesa-libGL \
    mesa-libEGL \
    fontconfig \
    glib2
```

## 📦 开发工具检查

### 1. Git
- [ ] Git 已安装
- [ ] Git 版本 2.0 或更高

**验证命令**:
```bash
git --version
```

**安装**:
- Windows: https://git-scm.com/download/win
- macOS: `brew install git`
- Linux: `sudo apt install git` 或 `sudo dnf install git`

### 2. 编译工具（可选，某些包可能需要）
- [ ] C/C++ 编译器已安装（如 gcc、clang 或 MSVC）

**验证命令**:
```bash
# Linux/macOS
gcc --version

# Windows (如果安装了 Visual Studio)
cl
```

## 🔐 权限检查

### 文件系统权限
- [ ] 有权限在安装目录创建文件
- [ ] 有权限在用户目录创建虚拟环境
- [ ] 有权限安装 Python 包（或使用虚拟环境）

**验证方法**:
```bash
# 尝试在项目目录创建测试文件
cd /path/to/Customer-Agent
touch test.txt
rm test.txt
```

### 管理员权限
- [ ] Windows 用户：不需要管理员权限（使用虚拟环境）
- [ ] Linux/macOS 用户：不要使用 sudo 安装（使用虚拟环境）

## 📋 配置准备

### 1. AI 服务配置
如果计划使用 AI 自动回复功能，请准备：

#### Coze AI
- [ ] Coze API Token
- [ ] Bot ID
- [ ] Personal Access Token

#### OpenAI
- [ ] API Key
- [ ] API Base URL（如果使用自定义端点）
- [ ] Model 名称（如 gpt-3.5-turbo）

#### Azure OpenAI
- [ ] API Key
- [ ] Endpoint URL
- [ ] Deployment Name
- [ ] API Version

### 2. 拼多多账号
- [ ] 拼多多商家账号用户名
- [ ] 商家账号密码
- [ ] 确保账号可以正常登录

## 🎯 安装方式选择

根据您的需求选择安装方式：

### 方式一：使用 uv（推荐）
- [ ] 我了解 uv 是一个快速的 Python 包管理器
- [ ] 我准备安装 uv

**优点**:
- 安装速度快
- 依赖解析准确
- 锁定文件保证版本一致

### 方式二：使用 pip
- [ ] 我更熟悉传统的 pip 工具
- [ ] 我的环境中 pip 已经配置好

**优点**:
- 传统方式，文档多
- 大多数人熟悉

### 方式三：开发模式
- [ ] 我计划修改源代码或参与开发
- [ ] 我需要安装开发工具（pytest、black等）

## 📱 可选工具

以下工具可以提升开发或使用体验：

- [ ] 代码编辑器（VS Code、PyCharm等）
- [ ] 终端模拟器（Windows Terminal、iTerm2等）
- [ ] API 测试工具（Postman、curl等）
- [ ] 数据库管理工具（DB Browser for SQLite）

## ✨ 准备工作完成

当您完成以上所有检查项后：

1. ✅ 所有必需项都已满足
2. ✅ 可选项根据需要配置
3. ✅ 已选择安装方式
4. ✅ 准备好配置信息

**下一步**: 前往 [安装指南](./INSTALLATION_GUIDE.md) 开始安装！

## 🚨 如果检查未通过

如果某些检查项未通过：

1. **Python 版本不符合**: 升级 Python 到 3.11+
2. **缺少系统库**: 按照上面的命令安装
3. **网络问题**: 配置代理或使用镜像源
4. **磁盘空间不足**: 清理磁盘或选择其他安装位置
5. **权限问题**: 使用虚拟环境，避免系统级安装

## 📞 需要帮助？

如果在检查过程中遇到问题：

1. 查看 [依赖问题快速修复指南](./DEPENDENCY_QUICK_FIX.md)
2. 访问 [GitHub Issues](https://github.com/C018/Customer-Agent/issues)
3. 加入社区频道（见 README 二维码）

---

**提示**: 完成此检查清单通常只需要 10-15 分钟，但可以避免几个小时的安装问题排查时间！

**最后更新**: 2025-12-08
