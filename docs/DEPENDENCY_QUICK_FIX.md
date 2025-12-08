# 依赖问题快速解决指南

## 快速诊断

### 1. 检查 Python 版本
```bash
python --version
```
**应该显示**: Python 3.11.x 或更高  
**如果不是**: 请升级 Python 到 3.11 或更高版本

### 2. 检查依赖安装
```bash
uv pip list
```
**应该包含**: playwright, websockets, requests, pyqt6, cozepy, openai 等

### 3. 检查浏览器驱动
```bash
uv run playwright install chrome --dry-run
```
**如果失败**: 运行 `uv run playwright install chrome`

## 常见错误及快速修复

### ❌ 错误 1: "playwright._impl._api_types.Error: Executable doesn't exist"

**原因**: 未安装浏览器驱动

**修复**:
```bash
uv run playwright install chrome
```

---

### ❌ 错误 2: "ImportError: DLL load failed" (Windows)

**原因**: 缺少 Visual C++ Redistributable

**修复**:
1. 下载并安装: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. 重启应用程序

---

### ❌ 错误 3: "ModuleNotFoundError: No module named 'XXX'"

**原因**: 依赖未正确安装

**修复**:
```bash
# 重新安装所有依赖
uv sync

# 或手动安装缺失的模块
uv pip install <模块名>
```

---

### ❌ 错误 4: WebSocket 连接失败

**原因**: Cookie 过期或网络问题

**修复**:
1. 在"账号管理"界面重新登录
2. 检查网络连接
3. 检查防火墙设置

---

### ❌ 错误 5: "sqlite3.OperationalError: unable to open database file"

**原因**: 数据库文件权限或路径问题

**修复**:
```bash
# 创建必要的目录
mkdir -p ./data

# Windows 用户
md data
```

---

### ❌ 错误 6: AI API 认证失败

**原因**: API Key 未配置或无效

**修复**:
1. 打开 `config.json` 文件
2. 检查并更新 API Key
3. 确认 API Key 有效且有足够额度

---

### ❌ 错误 7: "Rate limit exceeded"

**原因**: API 调用频率超限

**修复**:
1. 等待几分钟后重试
2. 减少自动回复频率
3. 升级 API 套餐

---

### ❌ 错误 8: 程序启动后界面空白

**原因**: PyQt6 初始化问题

**修复**:
```bash
# 重新安装 PyQt6 和相关组件
uv pip install --force-reinstall pyqt6 pyqt6-fluent-widgets
```

---

### ❌ 错误 9: "Failed to download browser" (Playwright)

**原因**: 网络连接问题或防火墙

**修复**:
```bash
# 使用国内镜像 (仅限中国大陆用户)
set PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/
uv run playwright install chrome
```

---

### ❌ 错误 10: 内存不足或程序卡死

**原因**: 资源占用过高

**修复**:
1. 关闭不必要的账号监控
2. 清理日志文件 (logs 目录)
3. 重启应用程序
4. 增加系统内存

---

## 完全重新安装

如果以上方法都无法解决问题，尝试完全重新安装:

```bash
# 1. 删除虚拟环境
rm -rf .venv   # Linux/Mac
rmdir /s .venv # Windows

# 2. 清理缓存
uv cache clean

# 3. 重新创建环境
uv venv

# 4. 安装依赖
uv sync

# 5. 安装浏览器驱动
uv run playwright install chrome

# 6. 验证安装
uv run python app.py
```

## 获取帮助

如果问题仍未解决:

1. **查看日志**: 检查 `logs` 目录下的日志文件
2. **提交 Issue**: https://github.com/C018/Customer-Agent/issues
3. **提供信息**:
   - Python 版本 (`python --version`)
   - 操作系统版本
   - 错误信息完整截图
   - 相关日志文件

## 预防性维护

定期执行以下操作可以避免大多数依赖问题:

```bash
# 每月一次：更新依赖
uv sync

# 每周一次：清理日志
# 删除 logs 目录下超过 30 天的日志文件

# 每次更新后：验证功能
uv run python -c "import playwright, websockets, requests, pyqt6, cozepy, openai; print('All OK')"
```

---

**提示**: 大多数依赖问题都是由于安装不完整或版本不匹配导致的。使用 `uv sync` 可以确保所有依赖版本正确匹配。
