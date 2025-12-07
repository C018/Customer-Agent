# AI Bot 配置指南

本系统支持三种AI Bot类型：Coze、OpenAI 和 Azure OpenAI。您可以根据需要选择合适的AI服务。

## 配置文件位置

配置文件位于项目根目录：`config.json`

如果文件不存在，系统会在首次运行时自动创建默认配置。

## 配置选项

### 1. 使用 Coze AI（默认）

```json
{
    "bot_type": "coze",
    "coze_api_base": "https://api.coze.cn",
    "coze_token": "你的Coze API Token",
    "coze_bot_id": "你的Coze Bot ID",
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

**配置说明：**
- `bot_type`: 必须设置为 `"coze"`
- `coze_api_base`: Coze API 基础地址
- `coze_token`: 从 [Coze 平台](https://www.coze.cn/) 获取的 API Token
- `coze_bot_id`: 在 Coze 平台创建的 Bot ID

### 2. 使用 OpenAI

```json
{
    "bot_type": "openai",
    "openai_api_key": "你的OpenAI API Key",
    "openai_api_base": "https://api.openai.com/v1",
    "openai_model": "gpt-3.5-turbo",
    "openai_max_tokens": 1000,
    "openai_temperature": 0.7,
    "openai_system_prompt": "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。",
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

**配置说明：**
- `bot_type`: 必须设置为 `"openai"`
- `openai_api_key`: 从 [OpenAI](https://platform.openai.com/) 获取的 API Key
- `openai_api_base`: OpenAI API 基础地址（可选，默认为官方地址）
- `openai_model`: 使用的模型名称（如 `gpt-3.5-turbo`、`gpt-4` 等）
- `openai_max_tokens`: 单次回复的最大token数
- `openai_temperature`: 温度参数（0-1），控制回复的随机性
- `openai_system_prompt`: 系统提示词，定义AI的角色和行为

**使用国内镜像或第三方API：**

如果您使用的是国内镜像或第三方OpenAI兼容API，可以修改 `openai_api_base`：

```json
{
    "bot_type": "openai",
    "openai_api_key": "你的API Key",
    "openai_api_base": "https://your-proxy-domain.com/v1",
    "openai_model": "gpt-3.5-turbo"
}
```

### 3. 使用 Azure OpenAI

```json
{
    "bot_type": "azure_openai",
    "azure_openai_api_key": "你的Azure OpenAI API Key",
    "azure_openai_endpoint": "https://your-resource-name.openai.azure.com",
    "azure_openai_api_version": "2024-02-15-preview",
    "azure_openai_deployment_name": "你的部署名称",
    "azure_openai_max_tokens": 1000,
    "azure_openai_temperature": 0.7,
    "azure_openai_system_prompt": "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。",
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

**配置说明：**
- `bot_type`: 必须设置为 `"azure_openai"`
- `azure_openai_api_key`: Azure OpenAI 的 API Key
- `azure_openai_endpoint`: Azure OpenAI 的端点地址
- `azure_openai_api_version`: API 版本（建议使用最新版本）
- `azure_openai_deployment_name`: 在 Azure 中创建的部署名称
- `azure_openai_max_tokens`: 单次回复的最大token数
- `azure_openai_temperature`: 温度参数（0-1），控制回复的随机性
- `azure_openai_system_prompt`: 系统提示词，定义AI的角色和行为

**获取 Azure OpenAI 配置信息：**

1. 登录 [Azure Portal](https://portal.azure.com/)
2. 找到您的 Azure OpenAI 资源
3. 在"密钥和终结点"页面获取：
   - API Key
   - 终结点（Endpoint）
4. 在"部署"页面获取您的部署名称

## 营业时间配置

所有bot类型都支持营业时间配置：

```json
{
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

- `start`: 营业开始时间（24小时制）
- `end`: 营业结束时间（24小时制）

在非营业时间，系统会自动发送非营业时间提示，而不会调用AI进行回复。

## 配置示例

### 完整的 OpenAI 配置示例

```json
{
    "bot_type": "openai",
    "openai_api_key": "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "openai_api_base": "https://api.openai.com/v1",
    "openai_model": "gpt-3.5-turbo",
    "openai_max_tokens": 1000,
    "openai_temperature": 0.7,
    "openai_system_prompt": "你是一个专业的拼多多商家客服助手。请礼貌、专业地回答客户的问题。对于商品相关的问题，请提供详细的信息。对于物流问题，请安抚客户并说明会尽快处理。",
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

### 完整的 Azure OpenAI 配置示例

```json
{
    "bot_type": "azure_openai",
    "azure_openai_api_key": "your-32-character-api-key",
    "azure_openai_endpoint": "https://your-resource-name.openai.azure.com",
    "azure_openai_api_version": "2024-02-15-preview",
    "azure_openai_deployment_name": "gpt-35-turbo",
    "azure_openai_max_tokens": 1000,
    "azure_openai_temperature": 0.7,
    "azure_openai_system_prompt": "你是一个专业的拼多多商家客服助手。请礼貌、专业地回答客户的问题。对于商品相关的问题，请提供详细的信息。对于物流问题，请安抚客户并说明会尽快处理。",
    "businessHours": {
        "start": "08:00",
        "end": "23:00"
    }
}
```

## 切换AI服务

要切换AI服务，只需修改 `config.json` 中的 `bot_type` 字段，并确保相应的配置项已正确填写。修改后需要重启应用程序。

## 注意事项

1. **API Key 安全**: 请妥善保管您的 API Key，不要将其提交到公开的代码仓库
2. **成本控制**: 使用 OpenAI 或 Azure OpenAI 会产生费用，建议设置合理的 `max_tokens` 值
3. **系统提示词**: 可以根据您的业务需求自定义 `system_prompt`，使AI的回复更符合您的需求
4. **模型选择**: 不同模型有不同的性能和成本，请根据需求选择
   - `gpt-3.5-turbo`: 性价比高，响应快
   - `gpt-4`: 能力更强，但成本更高

## 故障排除

### 1. Bot初始化失败

**错误信息**: "Failed to initialize OpenAI Bot"

**解决方案**:
- 检查API Key是否正确
- 检查网络连接
- 确认API余额充足

### 2. API调用失败

**错误信息**: "OpenAI API call failed"

**解决方案**:
- 检查API配置是否正确
- 查看日志获取详细错误信息
- 确认API服务状态正常

### 3. Azure OpenAI连接失败

**错误信息**: "Azure OpenAI endpoint is not configured"

**解决方案**:
- 确认已正确配置 `azure_openai_endpoint`
- 检查endpoint地址格式是否正确
- 确认Azure OpenAI资源已正确部署

## 获取帮助

如有问题，请查看：
- 项目 [GitHub Issues](https://github.com/C018/Customer-Agent/issues)
- 查看系统日志文件获取详细错误信息
