"""
OpenAI Bot implementation
Supports both OpenAI and Azure OpenAI
"""
from Agent.bot import Bot
from bridge.context import Context
from bridge.reply import Reply, ReplyType
from utils.logger import get_logger
from config import config
import json


class OpenAIBot(Bot):
    """OpenAI Bot for auto-reply"""
    
    def __init__(self):
        super().__init__()
        self.logger = get_logger("OpenAIBot")
        self.bot_type = config.get("bot_type", "openai")
        
        # 初始化OpenAI client
        try:
            from openai import OpenAI
            
            # 配置参数
            self.api_key = config.get("openai_api_key", "")
            self.api_base = config.get("openai_api_base", "https://api.openai.com/v1")
            self.model = config.get("openai_model", "gpt-3.5-turbo")
            self.max_tokens = config.get("openai_max_tokens", 1000)
            self.temperature = config.get("openai_temperature", 0.7)
            self.system_prompt = config.get("openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。")
            
            if not self.api_key:
                raise ValueError("OpenAI API key is not configured")
            
            # 创建客户端
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.api_base
            )
            
            self.logger.info(f"OpenAI Bot initialized with model: {self.model}")
            
        except ImportError:
            self.logger.error("openai package is not installed. Please install it with: pip install openai")
            raise
        except Exception as e:
            self.logger.error(f"Failed to initialize OpenAI Bot: {e}")
            raise
    
    def reply(self, context: Context) -> Reply:
        """
        生成AI回复
        
        Args:
            context: 消息上下文
            
        Returns:
            Reply对象
        """
        try:
            # 解析消息内容
            query = self._parse_content(context.content)
            
            if not query:
                return Reply(ReplyType.TEXT, "抱歉，我没有理解您的问题。")
            
            # 调用OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # 提取回复内容
            if response.choices and len(response.choices) > 0:
                reply_content = response.choices[0].message.content
                return Reply(ReplyType.TEXT, reply_content)
            else:
                return Reply(ReplyType.TEXT, "抱歉，我暂时无法回答您的问题。")
                
        except Exception as e:
            self.logger.error(f"OpenAI API call failed: {e}", exc_info=True)
            return Reply(ReplyType.TEXT, "抱歉，服务暂时不可用，请稍后再试。")
    
    def _parse_content(self, content: str) -> str:
        """
        解析消息内容
        
        Args:
            content: 原始消息内容（可能是JSON字符串）
            
        Returns:
            解析后的文本内容
        """
        try:
            # 尝试解析JSON格式
            if isinstance(content, str) and content.startswith('['):
                content_list = json.loads(content)
                if isinstance(content_list, list) and len(content_list) > 0:
                    # 提取文本内容
                    text_parts = []
                    for item in content_list:
                        if isinstance(item, dict) and item.get('type') == 'text':
                            text_parts.append(item.get('text', ''))
                    return ' '.join(text_parts)
            
            # 如果不是JSON或解析失败，直接返回原内容
            return str(content)
            
        except Exception as e:
            self.logger.warning(f"Failed to parse content: {e}")
            return str(content)


class AzureOpenAIBot(Bot):
    """Azure OpenAI Bot for auto-reply"""
    
    def __init__(self):
        super().__init__()
        self.logger = get_logger("AzureOpenAIBot")
        
        # 初始化Azure OpenAI client
        try:
            from openai import AzureOpenAI
            
            # 配置参数
            self.api_key = config.get("azure_openai_api_key", "")
            self.api_base = config.get("azure_openai_endpoint", "")
            self.api_version = config.get("azure_openai_api_version", "2024-02-15-preview")
            self.deployment_name = config.get("azure_openai_deployment_name", "")
            self.max_tokens = config.get("azure_openai_max_tokens", 1000)
            self.temperature = config.get("azure_openai_temperature", 0.7)
            self.system_prompt = config.get("azure_openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。")
            
            if not self.api_key:
                raise ValueError("Azure OpenAI API key is not configured")
            if not self.api_base:
                raise ValueError("Azure OpenAI endpoint is not configured")
            if not self.deployment_name:
                raise ValueError("Azure OpenAI deployment name is not configured")
            
            # 创建客户端
            self.client = AzureOpenAI(
                api_key=self.api_key,
                api_version=self.api_version,
                azure_endpoint=self.api_base
            )
            
            self.logger.info(f"Azure OpenAI Bot initialized with deployment: {self.deployment_name}")
            
        except ImportError:
            self.logger.error("openai package is not installed. Please install it with: pip install openai")
            raise
        except Exception as e:
            self.logger.error(f"Failed to initialize Azure OpenAI Bot: {e}")
            raise
    
    def reply(self, context: Context) -> Reply:
        """
        生成AI回复
        
        Args:
            context: 消息上下文
            
        Returns:
            Reply对象
        """
        try:
            # 解析消息内容
            query = self._parse_content(context.content)
            
            if not query:
                return Reply(ReplyType.TEXT, "抱歉，我没有理解您的问题。")
            
            # 调用Azure OpenAI API
            response = self.client.chat.completions.create(
                model=self.deployment_name,  # Azure uses deployment name as model
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            # 提取回复内容
            if response.choices and len(response.choices) > 0:
                reply_content = response.choices[0].message.content
                return Reply(ReplyType.TEXT, reply_content)
            else:
                return Reply(ReplyType.TEXT, "抱歉，我暂时无法回答您的问题。")
                
        except Exception as e:
            self.logger.error(f"Azure OpenAI API call failed: {e}", exc_info=True)
            return Reply(ReplyType.TEXT, "抱歉，服务暂时不可用，请稍后再试。")
    
    def _parse_content(self, content: str) -> str:
        """
        解析消息内容
        
        Args:
            content: 原始消息内容（可能是JSON字符串）
            
        Returns:
            解析后的文本内容
        """
        try:
            # 尝试解析JSON格式
            if isinstance(content, str) and content.startswith('['):
                content_list = json.loads(content)
                if isinstance(content_list, list) and len(content_list) > 0:
                    # 提取文本内容
                    text_parts = []
                    for item in content_list:
                        if isinstance(item, dict) and item.get('type') == 'text':
                            text_parts.append(item.get('text', ''))
                    return ' '.join(text_parts)
            
            # 如果不是JSON或解析失败，直接返回原内容
            return str(content)
            
        except Exception as e:
            self.logger.warning(f"Failed to parse content: {e}")
            return str(content)
