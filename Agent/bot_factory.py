"""
Bot factory
创建不同类型的Bot实例
"""
from config import config
from utils.logger import get_logger

logger = get_logger("BotFactory")


def create_bot():
    """
    创建一个bot实例
    :return: bot实例
    """
    bot_type = config.get("bot_type", "coze")
    
    try:
        if bot_type == "coze":
            from Agent.CozeAgent.bot import CozeBot
            logger.info("正在创建 Coze Bot...")
            return CozeBot()
        elif bot_type == "openai":
            from Agent.OpenAIAgent.bot import OpenAIBot
            logger.info("正在创建 OpenAI Bot...")
            return OpenAIBot()
        elif bot_type == "azure_openai":
            from Agent.OpenAIAgent.bot import AzureOpenAIBot
            logger.info("正在创建 Azure OpenAI Bot...")
            return AzureOpenAIBot()
        else:
            error_msg = f"不支持的 Bot 类型: {bot_type}。支持的类型: coze, openai, azure_openai"
            logger.error(error_msg)
            raise RuntimeError(error_msg)
    except ValueError as e:
        # 配置错误（如缺少必填项）
        logger.error(f"Bot 配置错误: {e}")
        raise ValueError(f"Bot 配置错误: {e}。请检查设置界面的配置。")
    except ImportError as e:
        # 依赖包缺失
        logger.error(f"Bot 依赖包缺失: {e}")
        raise ImportError(f"Bot 依赖包缺失: {e}。请安装相应的依赖包。")
    except Exception as e:
        # 其他错误
        logger.error(f"创建 Bot 失败: {e}", exc_info=True)
        raise RuntimeError(f"创建 Bot 失败: {e}")