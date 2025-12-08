# 依赖分析文档 (Dependency Analysis)

## 概述

本文档详细分析了拼多多智能客服系统的所有依赖项，包括它们的用途、版本要求以及潜在的依赖问题解决方案。

## 系统要求

### Python 版本
- **要求**: Python 3.11+
- **说明**: 项目使用了 Python 3.11 的新特性
- **验证**: `.python-version` 文件指定为 `3.11`

### 操作系统
- **推荐**: Windows 10/11
- **兼容性**: 理论上支持 Linux 和 macOS，但主要针对 Windows 开发和测试
- **说明**: 浏览器自动化功能在 Windows 上测试最充分

### 网络要求
- 稳定的网络连接（用于访问拼多多平台和 AI 服务）
- 能够访问以下服务（根据配置）:
  - Coze API
  - OpenAI API
  - Azure OpenAI API

## 核心依赖分析

### 1. Web 自动化和浏览器控制

#### playwright (>=1.52.0)
- **用途**: 浏览器自动化，用于自动登录拼多多商家平台
- **关键功能**:
  - 自动获取登录 cookies
  - 模拟真实用户操作
  - 反爬虫绕过
- **使用位置**:
  - `Channel/pinduoduo/pdd_login.py`: 实现拼多多自动登录
- **额外安装步骤**: 需要安装浏览器驱动
  ```bash
  uv run playwright install chrome
  ```
- **潜在问题**:
  - 首次使用需要下载 Chrome 浏览器（约 300MB）
  - 需要足够的磁盘空间
  - 某些防火墙可能阻止浏览器下载

### 2. 实时通信

#### websockets (>=10.4)
- **用途**: WebSocket 客户端，用于实时接收拼多多平台的消息
- **关键功能**:
  - 建立与拼多多消息服务器的 WebSocket 连接
  - 实时接收客户消息
  - 维护长连接
- **使用位置**:
  - `Channel/pinduoduo/pdd_chnnel.py`: 主要的 WebSocket 连接管理
  - `utils/resource_manager.py`: WebSocket 资源管理
- **潜在问题**:
  - 需要稳定的网络连接
  - 防火墙可能阻止 WebSocket 连接
  - 长时间连接可能需要心跳保活机制

### 3. HTTP 请求

#### requests (>=2.28.0)
- **用途**: HTTP 客户端，用于调用拼多多 API
- **关键功能**:
  - 发送消息
  - 获取用户信息
  - 获取店铺信息
  - 获取 token
- **使用位置**:
  - `Channel/pinduoduo/utils/API/`: 所有 API 调用
  - `ui/auto_reply_ui.py`: 账号监控
  - `ui/user_ui.py`: 用户界面请求
- **潜在问题**:
  - SSL 证书验证问题
  - 代理配置（如需要）

#### PySocks (>=1.7.1)
- **用途**: SOCKS 代理支持
- **关键功能**:
  - 为 requests 提供 SOCKS 代理支持
  - 支持 SOCKS4、SOCKS5 协议
- **使用场景**:
  - 需要通过代理访问拼多多 API
  - 网络受限环境
- **潜在问题**:
  - 仅在需要代理时使用
  - 如果不需要代理可以忽略

### 4. AI 服务集成

#### cozepy (>=0.15.0)
- **用途**: Coze AI 服务的官方 Python SDK
- **关键功能**:
  - 与 Coze Bot 进行对话
  - 管理用户会话
  - 处理 AI 回复
- **使用位置**:
  - `Agent/CozeAgent/`: Coze AI 代理实现
  - `Agent/CozeAgent/conversation_manager.py`: 对话管理
  - `Agent/CozeAgent/bot.py`: Bot 实现
- **配置要求**:
  - 需要 Coze API Token
  - 需要 Bot ID
  - 需要 Personal Access Token
- **潜在问题**:
  - API 配额限制
  - 网络延迟影响响应速度
  - Token 过期处理

#### openai (>=1.0.0)
- **用途**: OpenAI 和 Azure OpenAI 的官方 Python SDK
- **关键功能**:
  - 调用 GPT 模型生成回复
  - 支持 OpenAI 和 Azure OpenAI
  - 聊天完成接口
- **使用位置**:
  - `Agent/OpenAIAgent/bot.py`: OpenAI Bot 实现
  - 支持两种模式:
    - OpenAIBot: 标准 OpenAI API
    - AzureOpenAIBot: Azure OpenAI 服务
- **配置要求**:
  - OpenAI: API Key 和 Base URL
  - Azure: API Key、Endpoint、API Version 和 Deployment Name
- **潜在问题**:
  - API 费用
  - 速率限制
  - 网络连接稳定性
  - Token 限制

### 5. Web 框架

#### flask (>=3.1.0)
- **用途**: Web 框架（当前可能用于未来的 Web 界面）
- **关键功能**:
  - HTTP 服务器
  - 路由管理
  - 请求处理
- **当前状态**: 在依赖列表中，但代码中未见直接使用
- **潜在用途**: 可能用于未来的 Web 管理界面或 API 接口

#### flask-sqlalchemy (>=3.1.1)
- **用途**: Flask 的 SQLAlchemy 集成
- **关键功能**:
  - 简化 Flask 中的数据库操作
  - 提供 Flask 风格的 SQLAlchemy 接口
- **当前状态**: 在依赖列表中，但主要使用纯 SQLAlchemy

#### flask-cors (>=5.0.1)
- **用途**: Flask 的 CORS（跨域资源共享）支持
- **关键功能**:
  - 允许跨域请求
  - 配置 CORS 策略
- **当前状态**: 在依赖列表中，用于未来的 Web API

### 6. 图形界面

#### pyqt6 (>=6.9.0)
- **用途**: Qt 6 的 Python 绑定，提供桌面 GUI 框架
- **关键功能**:
  - 创建桌面应用程序界面
  - 窗口管理
  - 事件处理
  - 线程支持
- **使用位置**:
  - `app.py`: 应用程序入口
  - `ui/`: 所有 UI 模块
- **系统要求**:
  - Windows: 需要 Visual C++ Redistributable
  - Linux: 需要 Qt 依赖库
  - macOS: 通常开箱即用
- **潜在问题**:
  - 较大的安装包（约 100MB+）
  - 某些 Linux 发行版需要额外安装系统库
  - 高 DPI 显示支持

#### pyqt6-fluent-widgets[full] (>=1.8.1)
- **用途**: PyQt6 的 Fluent Design 组件库
- **关键功能**:
  - 现代化的 UI 组件
  - Fluent Design 风格
  - 丰富的控件和动画
- **使用位置**:
  - `ui/`: 所有界面模块使用 qfluentwidgets
  - 包括主窗口、设置、日志、关键词管理等
- **安装选项**: `[full]` 表示安装完整版本，包含所有可选功能
- **潜在问题**:
  - 依赖 PyQt6，版本需要匹配
  - 某些组件可能需要额外的资源文件

### 7. 数据库

#### sqlalchemy (间接依赖)
- **用途**: Python SQL 工具包和 ORM
- **关键功能**:
  - 数据库抽象层
  - ORM 映射
  - 连接池管理
  - 事务处理
- **使用位置**:
  - `database/models.py`: 数据模型定义
  - `database/db_manager.py`: 数据库管理器
- **数据库选择**: SQLite（无需额外安装）
- **数据模型**:
  - Channel: 渠道表
  - Shop: 店铺表
  - Account: 账号表
  - Keyword: 关键词表
- **潜在问题**:
  - SQLite 文件权限问题
  - 并发写入限制（SQLite 特性）
  - 数据库文件损坏恢复

## 依赖关系图

```
拼多多智能客服系统
│
├─── 浏览器自动化
│    └── playwright (Chrome 驱动)
│
├─── 实时通信
│    └── websockets
│
├─── HTTP 通信
│    ├── requests
│    └── PySocks (可选代理)
│
├─── AI 服务
│    ├── cozepy (Coze AI)
│    └── openai (OpenAI/Azure)
│
├─── Web 框架 (未来)
│    ├── flask
│    ├── flask-sqlalchemy
│    └── flask-cors
│
├─── 图形界面
│    ├── pyqt6
│    └── pyqt6-fluent-widgets[full]
│
└─── 数据存储
     └── sqlalchemy (SQLite)
```

## 依赖冲突分析

### 1. PyQt6 版本冲突
- **问题**: PyQt6 和 pyqt6-fluent-widgets 版本需要匹配
- **解决方案**: 使用 uv.lock 锁定版本，确保兼容性
- **验证**: 
  ```bash
  uv run python -c "from PyQt6.QtCore import QT_VERSION_STR; print(QT_VERSION_STR)"
  ```

### 2. OpenAI SDK 版本
- **问题**: OpenAI SDK 1.0.0+ 引入了重大 API 变更
- **当前状态**: 代码已适配新版 API
- **向下兼容**: 不支持 < 1.0.0 版本
- **验证**: 检查导入是否成功
  ```python
  from openai import OpenAI, AzureOpenAI
  ```

### 3. Python 版本要求
- **问题**: 某些依赖需要 Python 3.11+
- **影响**:
  - 使用了较新的类型注解特性
  - 某些标准库功能
- **验证**:
  ```bash
  python --version  # 应该显示 3.11.x 或更高
  ```

### 4. Playwright 浏览器驱动
- **问题**: 浏览器驱动需要单独安装
- **忘记安装的症状**: 
  ```
  playwright._impl._api_types.Error: Executable doesn't exist
  ```
- **解决方案**:
  ```bash
  uv run playwright install chrome
  ```

### 5. Flask 相关依赖
- **当前状态**: 已添加但未使用
- **影响**: 增加了不必要的依赖体积
- **建议**: 如果确认不使用 Web 界面，可以考虑移除

## 安装顺序建议

### 标准安装流程

```bash
# 1. 确认 Python 版本
python --version  # 应该是 3.11+

# 2. 安装 uv（依赖管理工具）
pip install uv

# 3. 创建虚拟环境
uv venv

# 4. 安装所有依赖
uv sync

# 5. 安装浏览器驱动
uv run playwright install chrome
```

### 开发环境安装

```bash
# 使用相同的流程，但确保 uv.lock 存在
uv sync  # 会使用 uv.lock 中锁定的版本
```

### 问题排查安装

```bash
# 如果遇到依赖问题，尝试：

# 1. 清理缓存
uv cache clean

# 2. 重新安装
rm -rf .venv
uv venv
uv sync

# 3. 手动安装浏览器驱动
uv run playwright install chrome --force
```

## 常见依赖问题及解决方案

### 1. Playwright 安装失败

**问题描述**:
```
Failed to download browser
Connection timeout
```

**可能原因**:
- 网络连接问题
- 防火墙拦截
- 磁盘空间不足

**解决方案**:
```bash
# 设置环境变量使用镜像
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/

# 然后重新安装
uv run playwright install chrome
```

### 2. PyQt6 运行时错误

**问题描述**:
```
ImportError: DLL load failed: The specified module could not be found.
```

**可能原因**:
- Windows 缺少 Visual C++ Redistributable
- 系统缺少必要的 DLL

**解决方案**:
- Windows: 安装 [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Linux: 
  ```bash
  # Ubuntu/Debian
  sudo apt-get install libxcb-xinerama0 libxcb-cursor0
  
  # Fedora
  sudo dnf install xcb-util-cursor
  ```

### 3. SQLAlchemy 数据库错误

**问题描述**:
```
sqlite3.OperationalError: unable to open database file
```

**可能原因**:
- 权限问题
- 数据库路径不存在
- 磁盘空间不足

**解决方案**:
```bash
# 确保数据库目录存在
mkdir -p ./data

# 检查权限
ls -la ./data

# 如果需要，修改权限
chmod 755 ./data
```

### 4. WebSocket 连接失败

**问题描述**:
```
websockets.exceptions.InvalidStatusCode: server rejected WebSocket connection: HTTP 403
```

**可能原因**:
- Token 过期
- Cookie 失效
- 网络限制

**解决方案**:
1. 重新登录获取新的 cookies
2. 检查网络连接
3. 确认防火墙设置

### 5. AI API 调用失败

**问题描述**:
```
openai.error.RateLimitError: Rate limit exceeded
openai.error.AuthenticationError: Invalid API key
```

**解决方案**:
1. 检查 API Key 配置
2. 确认账户额度
3. 实现重试机制（代码中已有）
4. 考虑降低请求频率

### 6. 内存不足

**问题描述**:
- 程序运行缓慢
- 进程被系统杀死

**可能原因**:
- 浏览器进程占用大量内存
- WebSocket 连接过多
- 日志文件过大

**解决方案**:
1. 限制浏览器数量
2. 定期清理日志
3. 实现资源管理器（代码中已有）
4. 增加系统内存

## 可选依赖

### 开发依赖
如果需要开发或测试，可能还需要:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
]
```

### 生产优化
生产环境可能需要:

```toml
[project.optional-dependencies]
prod = [
    "gunicorn>=21.0.0",  # 如果使用 Flask Web 界面
    "sentry-sdk>=1.0.0",  # 错误追踪
]
```

## 依赖更新策略

### 主要版本更新
- **playwright**: 关注浏览器兼容性更新
- **pyqt6**: 谨慎更新，可能影响 UI 组件
- **openai**: 关注 API 变更，可能需要代码调整
- **cozepy**: 关注 Coze 平台更新

### 安全更新
- 定期检查依赖的安全漏洞
- 使用 `pip-audit` 或 `safety` 工具
- 及时更新有安全问题的依赖

### 更新命令
```bash
# 查看可更新的依赖
uv pip list --outdated

# 更新特定依赖
uv add "package>=new_version"

# 更新 uv.lock
uv lock
```

## 系统资源要求

### 最低配置
- **CPU**: 双核处理器
- **内存**: 4GB RAM
- **磁盘**: 2GB 可用空间
- **网络**: 稳定的互联网连接

### 推荐配置
- **CPU**: 四核处理器或更好
- **内存**: 8GB RAM 或更多
- **磁盘**: 5GB 可用空间（包括浏览器和日志）
- **网络**: 高速稳定的互联网连接

### 资源占用分析
- **Python 进程**: ~200MB
- **Chrome 浏览器**: ~300-500MB（每个实例）
- **PyQt6 界面**: ~100-200MB
- **数据库**: < 100MB（取决于数据量）

## 依赖验证清单

安装完成后，使用以下清单验证依赖:

```bash
# 1. Python 版本
python --version

# 2. 核心依赖
uv run python -c "import playwright; print('Playwright OK')"
uv run python -c "import websockets; print('WebSockets OK')"
uv run python -c "import requests; print('Requests OK')"

# 3. AI 依赖
uv run python -c "import cozepy; print('Coze OK')"
uv run python -c "import openai; print('OpenAI OK')"

# 4. UI 依赖
uv run python -c "from PyQt6.QtWidgets import QApplication; print('PyQt6 OK')"
uv run python -c "from qfluentwidgets import FluentWindow; print('FluentWidgets OK')"

# 5. 数据库
uv run python -c "import sqlalchemy; print('SQLAlchemy OK')"

# 6. 浏览器驱动
uv run playwright install chrome --dry-run
```

## 总结

### 关键依赖（必需）
1. **playwright** - 浏览器自动化
2. **websockets** - 实时消息接收
3. **requests** - API 调用
4. **pyqt6** + **pyqt6-fluent-widgets** - 图形界面
5. **sqlalchemy** - 数据库操作

### AI 依赖（至少选择一个）
1. **cozepy** - Coze AI
2. **openai** - OpenAI 或 Azure OpenAI

### 可选依赖
1. **PySocks** - SOCKS 代理支持
2. **flask** 系列 - Web 界面（未来功能）

### 安装建议
1. 使用 `uv` 作为依赖管理工具
2. 严格遵循 Python 3.11+ 版本要求
3. 安装后必须运行 `playwright install chrome`
4. 定期更新依赖以获取安全修复
5. 在生产环境使用 `uv.lock` 锁定版本

### 常见问题避免
1. 先确认 Python 版本再安装
2. 不要忘记安装浏览器驱动
3. 确保网络连接稳定
4. Windows 用户安装 Visual C++ Redistributable
5. 配置正确的 API Keys 和 Tokens

---

**最后更新**: 2025-12-08  
**文档版本**: 1.0.0  
**项目版本**: 1.0.0
