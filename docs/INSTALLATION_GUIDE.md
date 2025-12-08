# 安装指南 (Installation Guide)

本指南提供了拼多多智能客服系统的详细安装步骤，涵盖不同操作系统和安装方式。

## 目录

- [前提条件](#前提条件)
- [方式一：使用 uv（推荐）](#方式一使用-uv推荐)
- [方式二：使用 pip](#方式二使用-pip)
- [方式三：开发环境安装](#方式三开发环境安装)
- [验证安装](#验证安装)
- [常见问题](#常见问题)

## 前提条件

### 1. Python 版本

**要求**: Python 3.11 或更高版本

**检查当前版本**:
```bash
python --version
```

**如果版本不符合要求**:
- Windows: 从 [python.org](https://www.python.org/downloads/) 下载安装
- macOS: 
  ```bash
  brew install python@3.11
  ```
- Linux (Ubuntu/Debian):
  ```bash
  sudo apt update
  sudo apt install python3.11 python3.11-venv python3.11-dev
  ```

### 2. Git

**检查是否安装**:
```bash
git --version
```

**如果未安装**:
- Windows: 从 [git-scm.com](https://git-scm.com/download/win) 下载安装
- macOS: 
  ```bash
  brew install git
  ```
- Linux:
  ```bash
  sudo apt install git  # Ubuntu/Debian
  sudo yum install git  # CentOS/RHEL
  ```

### 3. 系统依赖

#### Windows
- Visual C++ Redistributable:
  - [下载链接](https://aka.ms/vs/17/release/vc_redist.x64.exe)
  - 安装后需要重启

#### Linux (Ubuntu/Debian)
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

#### Linux (Fedora/RHEL)
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

#### macOS
```bash
# 通常不需要额外依赖
# 如果遇到问题，可能需要安装 Xcode Command Line Tools
xcode-select --install
```

## 方式一：使用 uv（推荐）

uv 是一个快速的 Python 包管理器，推荐使用。

### 步骤 1: 克隆仓库

```bash
git clone https://github.com/C018/Customer-Agent.git
cd Customer-Agent
```

### 步骤 2: 安装 uv

```bash
pip install uv
```

或者使用 curl（Unix 系统）:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 步骤 3: 创建虚拟环境

```bash
uv venv
```

这将创建一个 `.venv` 目录。

### 步骤 4: 激活虚拟环境

**Windows (PowerShell)**:
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**:
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS**:
```bash
source .venv/bin/activate
```

### 步骤 5: 安装依赖

```bash
uv sync
```

这将安装 `pyproject.toml` 中定义的所有依赖，并使用 `uv.lock` 确保版本一致。

### 步骤 6: 安装浏览器驱动

```bash
uv run playwright install chrome
```

**注意**: 这一步会下载 Chrome 浏览器（约 300MB），请确保网络连接稳定。

**如果下载失败（中国大陆用户）**:
```bash
# Windows (PowerShell)
$env:PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright/"
uv run playwright install chrome

# Windows (CMD)
set PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/
uv run playwright install chrome

# Linux/macOS
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/
uv run playwright install chrome
```

### 步骤 7: 验证安装

```bash
uv run python app.py
```

如果一切正常，应该会启动图形界面。

## 方式二：使用 pip

如果你更熟悉 pip，可以使用这种方式。

### 步骤 1-2: 克隆仓库（同上）

```bash
git clone https://github.com/C018/Customer-Agent.git
cd Customer-Agent
```

### 步骤 3: 创建虚拟环境

```bash
python -m venv .venv
```

### 步骤 4: 激活虚拟环境

**Windows (PowerShell)**:
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**:
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS**:
```bash
source .venv/bin/activate
```

### 步骤 5: 升级 pip

```bash
python -m pip install --upgrade pip
```

### 步骤 6: 安装依赖

**使用 requirements.txt**:
```bash
pip install -r requirements.txt
```

**或直接从 pyproject.toml 安装**:
```bash
pip install -e .
```

### 步骤 7: 安装浏览器驱动

```bash
playwright install chrome
```

### 步骤 8: 验证安装

```bash
python app.py
```

## 方式三：开发环境安装

如果你要参与开发，推荐这种方式。

### 完整安装（开发模式）

```bash
# 1. 克隆仓库
git clone https://github.com/C018/Customer-Agent.git
cd Customer-Agent

# 2. 安装 uv（如果还没有）
pip install uv

# 3. 创建开发环境
uv venv

# 4. 激活环境（根据操作系统选择）
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate      # Windows

# 5. 安装所有依赖（包括开发依赖）
uv sync

# 6. 安装浏览器驱动
uv run playwright install chrome

# 7. 安装额外的开发工具（可选）
uv pip install pytest black flake8 mypy

# 8. 验证安装
python app.py
```

## 验证安装

运行以下命令验证所有依赖是否正确安装：

```bash
# 验证 Python 版本
python --version

# 验证核心库
python -c "import playwright; print('✓ Playwright')"
python -c "import websockets; print('✓ WebSockets')"
python -c "import requests; print('✓ Requests')"
python -c "import cozepy; print('✓ Coze')"
python -c "import openai; print('✓ OpenAI')"
python -c "from PyQt6.QtWidgets import QApplication; print('✓ PyQt6')"
python -c "from qfluentwidgets import FluentWindow; print('✓ FluentWidgets')"
python -c "import sqlalchemy; print('✓ SQLAlchemy')"

# 验证浏览器驱动
playwright install chrome --dry-run
```

如果所有命令都成功执行，说明安装完成。

## 卸载

如果需要完全卸载：

```bash
# 1. 停用虚拟环境
deactivate

# 2. 删除虚拟环境目录
rm -rf .venv  # Linux/macOS
rmdir /s .venv  # Windows

# 3. 删除浏览器驱动（可选）
# Windows: %USERPROFILE%\AppData\Local\ms-playwright
# macOS: ~/Library/Caches/ms-playwright
# Linux: ~/.cache/ms-playwright

# 4. 删除项目目录（如果需要）
cd ..
rm -rf Customer-Agent  # Linux/macOS
rmdir /s Customer-Agent  # Windows
```

## 常见问题

### Q1: "python: command not found" 或 "python3: command not found"

**解决方案**:
- 确保 Python 已正确安装
- Windows 用户需要在安装时勾选 "Add Python to PATH"
- Linux/macOS 用户可能需要使用 `python3` 而不是 `python`

### Q2: "pip: command not found"

**解决方案**:
```bash
python -m ensurepip --upgrade
```

### Q3: 权限错误（Permission denied）

**解决方案**:
- Linux/macOS: 不要使用 `sudo`，使用虚拟环境
- Windows: 以管理员身份运行命令提示符

### Q4: 虚拟环境激活失败（Windows PowerShell）

**错误**: "无法加载文件，因为在此系统上禁止运行脚本"

**解决方案**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q5: Playwright 下载超时

**解决方案**:
- 使用镜像源（见上文步骤 6）
- 检查网络连接
- 如果在公司网络，可能需要配置代理

### Q6: PyQt6 导入错误（Linux）

**错误**: "ImportError: libxcb-cursor.so.0"

**解决方案**:
```bash
# Ubuntu/Debian
sudo apt install libxcb-cursor0

# Fedora/RHEL
sudo dnf install xcb-util-cursor
```

### Q7: 安装速度慢

**解决方案**:
```bash
# 使用国内镜像（中国大陆用户）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q8: 空间不足

**解决方案**:
- 清理 pip 缓存: `pip cache purge`
- 清理 uv 缓存: `uv cache clean`
- 确保至少有 2GB 可用空间

## 更新依赖

### 更新到最新版本

```bash
# 使用 uv
uv sync

# 使用 pip
pip install -r requirements.txt --upgrade
```

### 更新特定包

```bash
# 使用 uv
uv add "package_name>=new_version"

# 使用 pip
pip install --upgrade package_name
```

## 技术支持

如果遇到安装问题：

1. **查看文档**: 
   - [依赖分析文档](./DEPENDENCY_ANALYSIS.md)
   - [快速修复指南](./DEPENDENCY_QUICK_FIX.md)

2. **提交 Issue**:
   - 访问 [GitHub Issues](https://github.com/C018/Customer-Agent/issues)
   - 提供以下信息:
     - Python 版本 (`python --version`)
     - 操作系统和版本
     - 完整的错误信息
     - 已尝试的解决方案

3. **社区支持**:
   - 加入频道（见 README 中的二维码）

---

**最后更新**: 2025-12-08  
**适用版本**: 1.0.0
