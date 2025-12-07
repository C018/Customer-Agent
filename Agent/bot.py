"""
自动回复聊天机器人抽象类
"""


from bridge.context import Context
from bridge.reply import Reply


class Bot(object):
    def reply(self, context: Context) -> Reply:
        """
        bot auto-reply content
        :param context: Context object containing message information
        :return: reply content
        """
        raise NotImplementedError