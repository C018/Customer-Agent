# 设置界面

import json
import os
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, QWidget, QLabel, 
                            QFormLayout, QGroupBox, QMessageBox)
from PyQt6.QtGui import QFont
from qfluentwidgets import (CardWidget, SubtitleLabel, CaptionLabel, BodyLabel, 
                           PrimaryPushButton, PushButton, StrongBodyLabel, 
                           LineEdit, ComboBox, ScrollArea, FluentIcon as FIF,
                           InfoBar, InfoBarPosition, TextEdit, PasswordLineEdit,
                           TimePicker)
from PyQt6.QtCore import QTime
from utils.logger import get_logger
from config import config


class AIServiceSelectorCard(CardWidget):
    """AI服务选择卡片"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)
        
        # 卡片标题
        title_label = StrongBodyLabel("AI 服务选择")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # AI服务类型选择
        self.bot_type_combo = ComboBox()
        self.bot_type_combo.addItems(["Coze", "OpenAI", "Azure OpenAI"])
        self.bot_type_combo.setCurrentIndex(0)
        form_layout.addRow("AI 服务类型:", self.bot_type_combo)
        
        layout.addLayout(form_layout)
        
        # 说明文本
        description_label = CaptionLabel(
            "选择您要使用的 AI 服务类型。\n"
            "Coze: 使用 Coze 平台的 AI 服务\n"
            "OpenAI: 使用 OpenAI 的 GPT 模型\n"
            "Azure OpenAI: 使用 Azure 部署的 OpenAI 服务"
        )
        description_label.setStyleSheet("color: #666; padding: 8px 0;")
        layout.addWidget(description_label)
    
    def getConfig(self) -> dict:
        """获取配置"""
        bot_type_map = {
            "Coze": "coze",
            "OpenAI": "openai",
            "Azure OpenAI": "azure_openai"
        }
        return {
            "bot_type": bot_type_map.get(self.bot_type_combo.currentText(), "coze")
        }
    
    def setConfig(self, config: dict):
        """设置配置"""
        bot_type = config.get("bot_type", "coze")
        type_map = {
            "coze": "Coze",
            "openai": "OpenAI",
            "azure_openai": "Azure OpenAI"
        }
        display_name = type_map.get(bot_type, "Coze")
        index = self.bot_type_combo.findText(display_name)
        if index >= 0:
            self.bot_type_combo.setCurrentIndex(index)


class CozeConfigCard(CardWidget):
    """Coze配置卡片"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)
        
        # 卡片标题
        title_label = StrongBodyLabel("Coze AI 配置")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # API Base URL
        self.api_base_edit = LineEdit()
        self.api_base_edit.setPlaceholderText("https://api.coze.cn")
        self.api_base_edit.setText("https://api.coze.cn")
        form_layout.addRow("API Base URL:", self.api_base_edit)
        
        # API Token
        self.api_token_edit = PasswordLineEdit()
        self.api_token_edit.setPlaceholderText("输入您的 Coze API Token")
        form_layout.addRow("API Token:", self.api_token_edit)
        
        # Bot ID
        self.bot_id_edit = LineEdit()
        self.bot_id_edit.setPlaceholderText("输入您的 Bot ID")
        form_layout.addRow("Bot ID:", self.bot_id_edit)
                
        layout.addLayout(form_layout)
        
        # 说明文本
        description_label = CaptionLabel(
            "请在 Coze 平台获取您的 API Token 和 Bot ID。\n"
            "API Token 用于身份验证，Bot ID 用于指定使用的特定机器人。"
        )
        description_label.setStyleSheet("color: #666; padding: 8px 0;")
        layout.addWidget(description_label)
    
    def getConfig(self) -> dict:
        """获取配置"""
        return {
            "coze_api_base": self.api_base_edit.text().strip() or "https://api.coze.cn",
            "coze_token": self.api_token_edit.text().strip(),
            "coze_bot_id": self.bot_id_edit.text().strip()
        }
    
    def setConfig(self, config: dict):
        """设置配置"""
        self.api_base_edit.setText(config.get("coze_api_base", "https://api.coze.cn"))
        self.api_token_edit.setText(config.get("coze_token", ""))
        self.bot_id_edit.setText(config.get("coze_bot_id", ""))


class OpenAIConfigCard(CardWidget):
    """OpenAI配置卡片"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)
        
        # 卡片标题
        title_label = StrongBodyLabel("OpenAI 配置")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # API Key
        self.api_key_edit = PasswordLineEdit()
        self.api_key_edit.setPlaceholderText("输入您的 OpenAI API Key")
        form_layout.addRow("API Key:", self.api_key_edit)
        
        # API Base URL
        self.api_base_edit = LineEdit()
        self.api_base_edit.setPlaceholderText("https://api.openai.com/v1")
        self.api_base_edit.setText("https://api.openai.com/v1")
        form_layout.addRow("API Base URL:", self.api_base_edit)
        
        # Model
        self.model_edit = LineEdit()
        self.model_edit.setPlaceholderText("gpt-3.5-turbo")
        self.model_edit.setText("gpt-3.5-turbo")
        form_layout.addRow("Model:", self.model_edit)
        
        # Max Tokens
        self.max_tokens_edit = LineEdit()
        self.max_tokens_edit.setPlaceholderText("1000")
        self.max_tokens_edit.setText("1000")
        form_layout.addRow("Max Tokens:", self.max_tokens_edit)
        
        # Temperature
        self.temperature_edit = LineEdit()
        self.temperature_edit.setPlaceholderText("0.7")
        self.temperature_edit.setText("0.7")
        form_layout.addRow("Temperature:", self.temperature_edit)
        
        # System Prompt
        self.system_prompt_edit = TextEdit()
        self.system_prompt_edit.setPlaceholderText("你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。")
        self.system_prompt_edit.setMaximumHeight(100)
        form_layout.addRow("System Prompt:", self.system_prompt_edit)
        
        layout.addLayout(form_layout)
        
        # 说明文本
        description_label = CaptionLabel(
            "请在 OpenAI 平台获取您的 API Key。\n"
            "支持自定义 API Base URL、模型和参数配置。"
        )
        description_label.setStyleSheet("color: #666; padding: 8px 0;")
        layout.addWidget(description_label)
    
    def getConfig(self) -> dict:
        """获取配置"""
        try:
            max_tokens = int(self.max_tokens_edit.text() or "1000")
        except ValueError:
            max_tokens = 1000
        
        try:
            temperature = float(self.temperature_edit.text() or "0.7")
        except ValueError:
            temperature = 0.7
        
        return {
            "openai_api_key": self.api_key_edit.text().strip(),
            "openai_api_base": self.api_base_edit.text().strip() or "https://api.openai.com/v1",
            "openai_model": self.model_edit.text().strip() or "gpt-3.5-turbo",
            "openai_max_tokens": max_tokens,
            "openai_temperature": temperature,
            "openai_system_prompt": self.system_prompt_edit.toPlainText().strip() or "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"
        }
    
    def setConfig(self, config: dict):
        """设置配置"""
        self.api_key_edit.setText(config.get("openai_api_key", ""))
        self.api_base_edit.setText(config.get("openai_api_base", "https://api.openai.com/v1"))
        self.model_edit.setText(config.get("openai_model", "gpt-3.5-turbo"))
        self.max_tokens_edit.setText(str(config.get("openai_max_tokens", 1000)))
        self.temperature_edit.setText(str(config.get("openai_temperature", 0.7)))
        self.system_prompt_edit.setPlainText(config.get("openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"))


class AzureOpenAIConfigCard(CardWidget):
    """Azure OpenAI配置卡片"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)
        
        # 卡片标题
        title_label = StrongBodyLabel("Azure OpenAI 配置")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # API Key
        self.api_key_edit = PasswordLineEdit()
        self.api_key_edit.setPlaceholderText("输入您的 Azure OpenAI API Key")
        form_layout.addRow("API Key:", self.api_key_edit)
        
        # Endpoint
        self.endpoint_edit = LineEdit()
        self.endpoint_edit.setPlaceholderText("https://your-resource.openai.azure.com/")
        form_layout.addRow("Endpoint:", self.endpoint_edit)
        
        # API Version
        self.api_version_edit = LineEdit()
        self.api_version_edit.setPlaceholderText("2024-02-15-preview")
        self.api_version_edit.setText("2024-02-15-preview")
        form_layout.addRow("API Version:", self.api_version_edit)
        
        # Deployment Name
        self.deployment_name_edit = LineEdit()
        self.deployment_name_edit.setPlaceholderText("输入您的部署名称")
        form_layout.addRow("Deployment Name:", self.deployment_name_edit)
        
        # Max Tokens
        self.max_tokens_edit = LineEdit()
        self.max_tokens_edit.setPlaceholderText("1000")
        self.max_tokens_edit.setText("1000")
        form_layout.addRow("Max Tokens:", self.max_tokens_edit)
        
        # Temperature
        self.temperature_edit = LineEdit()
        self.temperature_edit.setPlaceholderText("0.7")
        self.temperature_edit.setText("0.7")
        form_layout.addRow("Temperature:", self.temperature_edit)
        
        # System Prompt
        self.system_prompt_edit = TextEdit()
        self.system_prompt_edit.setPlaceholderText("你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。")
        self.system_prompt_edit.setMaximumHeight(100)
        form_layout.addRow("System Prompt:", self.system_prompt_edit)
        
        layout.addLayout(form_layout)
        
        # 说明文本
        description_label = CaptionLabel(
            "请在 Azure 门户获取您的 API Key、Endpoint 和 Deployment Name。\n"
            "支持自定义 API 版本和参数配置。"
        )
        description_label.setStyleSheet("color: #666; padding: 8px 0;")
        layout.addWidget(description_label)
    
    def getConfig(self) -> dict:
        """获取配置"""
        try:
            max_tokens = int(self.max_tokens_edit.text() or "1000")
        except ValueError:
            max_tokens = 1000
        
        try:
            temperature = float(self.temperature_edit.text() or "0.7")
        except ValueError:
            temperature = 0.7
        
        return {
            "azure_openai_api_key": self.api_key_edit.text().strip(),
            "azure_openai_endpoint": self.endpoint_edit.text().strip(),
            "azure_openai_api_version": self.api_version_edit.text().strip() or "2024-02-15-preview",
            "azure_openai_deployment_name": self.deployment_name_edit.text().strip(),
            "azure_openai_max_tokens": max_tokens,
            "azure_openai_temperature": temperature,
            "azure_openai_system_prompt": self.system_prompt_edit.toPlainText().strip() or "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"
        }
    
    def setConfig(self, config: dict):
        """设置配置"""
        self.api_key_edit.setText(config.get("azure_openai_api_key", ""))
        self.endpoint_edit.setText(config.get("azure_openai_endpoint", ""))
        self.api_version_edit.setText(config.get("azure_openai_api_version", "2024-02-15-preview"))
        self.deployment_name_edit.setText(config.get("azure_openai_deployment_name", ""))
        self.max_tokens_edit.setText(str(config.get("azure_openai_max_tokens", 1000)))
        self.temperature_edit.setText(str(config.get("azure_openai_temperature", 0.7)))
        self.system_prompt_edit.setPlainText(config.get("azure_openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"))


class BusinessHoursCard(CardWidget):
    """业务时间配置卡片"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(16)
        
        # 卡片标题
        title_label = StrongBodyLabel("业务时间设置")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        layout.addWidget(title_label)
        
        # 表单布局
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # 开始时间
        self.start_time_picker = TimePicker()
        self.start_time_picker.setTime(QTime(8, 0))  # 默认8:00
        form_layout.addRow("开始时间:", self.start_time_picker)
        
        # 结束时间
        self.end_time_picker = TimePicker()
        self.end_time_picker.setTime(QTime(23, 0))  # 默认23:00
        form_layout.addRow("结束时间:", self.end_time_picker)
        
        layout.addLayout(form_layout)
        
        # 说明文本
        description_label = CaptionLabel(
            "设置AI客服的工作时间。在工作时间内，系统将自动响应客户消息。\n"
            "在非工作时间，系统将不会自动回复。"
        )
        description_label.setStyleSheet("color: #666; padding: 8px 0;")
        layout.addWidget(description_label)
    
    def getConfig(self) -> dict:
        """获取配置"""
        return {
            "businessHours": {
                "start": self.start_time_picker.getTime().toString("HH:mm"),
                "end": self.end_time_picker.getTime().toString("HH:mm")
            }
        }
    
    def setConfig(self, config: dict):
        """设置配置"""
        business_hours = config.get("businessHours", {})
        
        # 解析开始时间
        start_time_str = business_hours.get("start", "08:00")
        start_time = QTime.fromString(start_time_str, "HH:mm")
        if start_time.isValid():
            self.start_time_picker.setTime(start_time)
        
        # 解析结束时间
        end_time_str = business_hours.get("end", "23:00")
        end_time = QTime.fromString(end_time_str, "HH:mm")
        if end_time.isValid():
            self.end_time_picker.setTime(end_time)


class SettingUI(QFrame):
    """设置界面"""
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.logger = get_logger("SettingUI")
        self.setupUI()
        self.loadConfig()
        
        # 设置对象名
        self.setObjectName("设置")
    
    def setupUI(self):
        """设置主界面UI"""
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)
        
        # 创建头部区域
        header_widget = self.createHeaderWidget()
        
        # 创建内容区域
        content_widget = self.createContentWidget()
        
        # 连接按钮信号
        self.save_btn.clicked.connect(self.onSaveConfig)
        self.reset_btn.clicked.connect(self.onResetConfig)
        
        # 添加到主布局
        main_layout.addWidget(header_widget)
        main_layout.addWidget(content_widget, 1)
    
    def createHeaderWidget(self):
        """创建头部区域"""
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(20)
        
        # 标题
        title_label = SubtitleLabel("系统设置")
        title_label.setFont(QFont("Microsoft YaHei", 18, QFont.Weight.Bold))
        
        # 描述
        description_label = CaptionLabel("配置AI客服的基本参数和工作时间")
        description_label.setStyleSheet("color: #666;")
        
        # 左侧标题区域
        title_area = QWidget()
        title_layout = QVBoxLayout(title_area)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setSpacing(5)
        title_layout.addWidget(title_label)
        title_layout.addWidget(description_label)
        
        # 按钮区域
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(10)
        
        # 重置按钮
        self.reset_btn = PushButton("重置")
        self.reset_btn.setIcon(FIF.UPDATE)
        self.reset_btn.setFixedSize(80, 40)
        
        # 保存按钮
        self.save_btn = PrimaryPushButton("保存")
        self.save_btn.setIcon(FIF.SAVE)
        self.save_btn.setFixedSize(100, 40)
        
        buttons_layout.addWidget(self.reset_btn)
        buttons_layout.addWidget(self.save_btn)
        
        # 添加到头部布局
        header_layout.addWidget(title_area)
        header_layout.addStretch()
        header_layout.addWidget(buttons_widget)
        
        return header_widget
    
    def createContentWidget(self):
        """创建内容区域"""
        # 滚动区域
        scroll_area = ScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # 去除边框
        scroll_area.setStyleSheet("""
            ScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        # 内容容器
        content_container = QWidget()
        content_layout = QVBoxLayout(content_container)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # 创建配置卡片
        self.ai_selector_card = AIServiceSelectorCard()
        self.coze_config_card = CozeConfigCard()
        self.openai_config_card = OpenAIConfigCard()
        self.azure_openai_config_card = AzureOpenAIConfigCard()
        self.business_hours_card = BusinessHoursCard()
        
        # 连接AI服务选择器信号
        self.ai_selector_card.bot_type_combo.currentTextChanged.connect(self.onAIServiceChanged)
        
        # 添加到布局
        content_layout.addWidget(self.ai_selector_card)
        content_layout.addWidget(self.coze_config_card)
        content_layout.addWidget(self.openai_config_card)
        content_layout.addWidget(self.azure_openai_config_card)
        content_layout.addWidget(self.business_hours_card)
        content_layout.addStretch()
        
        # 设置容器样式
        content_container.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border: none;
            }
        """)
        
        scroll_area.setWidget(content_container)
        
        return scroll_area
    
    def onAIServiceChanged(self, service_name: str):
        """当AI服务类型改变时，显示/隐藏相应的配置卡片"""
        # 隐藏所有AI配置卡片
        self.coze_config_card.hide()
        self.openai_config_card.hide()
        self.azure_openai_config_card.hide()
        
        # 根据选择显示对应的配置卡片
        if service_name == "Coze":
            self.coze_config_card.show()
        elif service_name == "OpenAI":
            self.openai_config_card.show()
        elif service_name == "Azure OpenAI":
            self.azure_openai_config_card.show()
    
    def loadConfig(self):
        """从config模块加载配置"""
        try:            
            loaded_config = {
                "bot_type": config.get("bot_type", "coze"),
                "coze_api_base": config.get("coze_api_base", "https://api.coze.cn"),
                "coze_token": config.get("coze_token", ""),
                "coze_bot_id": config.get("coze_bot_id", ""),
                "openai_api_key": config.get("openai_api_key", ""),
                "openai_api_base": config.get("openai_api_base", "https://api.openai.com/v1"),
                "openai_model": config.get("openai_model", "gpt-3.5-turbo"),
                "openai_max_tokens": config.get("openai_max_tokens", 1000),
                "openai_temperature": config.get("openai_temperature", 0.7),
                "openai_system_prompt": config.get("openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"),
                "azure_openai_api_key": config.get("azure_openai_api_key", ""),
                "azure_openai_endpoint": config.get("azure_openai_endpoint", ""),
                "azure_openai_api_version": config.get("azure_openai_api_version", "2024-02-15-preview"),
                "azure_openai_deployment_name": config.get("azure_openai_deployment_name", ""),
                "azure_openai_max_tokens": config.get("azure_openai_max_tokens", 1000),
                "azure_openai_temperature": config.get("azure_openai_temperature", 0.7),
                "azure_openai_system_prompt": config.get("azure_openai_system_prompt", "你是一个专业的电商客服助手，请礼貌、专业地回答客户的问题。"),
                "businessHours": config.get("businessHours", {"start": "08:00", "end": "23:00"})
            }
            
            # 验证并设置配置
            self._validateAndSetConfig(loaded_config)
            self.logger.info("配置加载成功")
            
        except Exception as e:
            self.logger.error(f"加载配置失败: {e}")
            QMessageBox.warning(self, "加载失败", f"加载配置失败：{str(e)}")
            self._loadDefaultConfig()
    
    def _loadDefaultConfig(self):
        """加载默认配置"""
        from config import config_base
        
        self.ai_selector_card.setConfig(config_base)
        self.coze_config_card.setConfig(config_base)
        self.openai_config_card.setConfig(config_base)
        self.azure_openai_config_card.setConfig(config_base)
        self.business_hours_card.setConfig(config_base)
        
        # 根据默认配置显示相应的卡片
        self.onAIServiceChanged(self.ai_selector_card.bot_type_combo.currentText())
        self.logger.info("已加载默认配置")
    
    def _validateAndSetConfig(self, config_data):
        """验证并设置配置"""
        # 设置到界面
        self.ai_selector_card.setConfig(config_data)
        self.coze_config_card.setConfig(config_data)
        self.openai_config_card.setConfig(config_data)
        self.azure_openai_config_card.setConfig(config_data)
        self.business_hours_card.setConfig(config_data)
        
        # 根据配置的AI类型显示相应的卡片
        self.onAIServiceChanged(self.ai_selector_card.bot_type_combo.currentText())
    
    def onSaveConfig(self):
        """保存配置到config模块"""
        try:
            # 获取AI服务选择配置
            ai_selector_config = self.ai_selector_card.getConfig()
            bot_type = ai_selector_config.get("bot_type", "coze")
            
            # 获取所有AI服务配置
            coze_config = self.coze_config_card.getConfig()
            openai_config = self.openai_config_card.getConfig()
            azure_openai_config = self.azure_openai_config_card.getConfig()
            business_config = self.business_hours_card.getConfig()
            
            # 合并所有配置
            new_config = {
                **ai_selector_config,
                **coze_config,
                **openai_config,
                **azure_openai_config,
                **business_config
            }
            
            # 根据选择的AI类型验证必填项
            if bot_type == "coze":
                if not new_config.get("coze_token"):
                    QMessageBox.warning(self, "配置错误", "请输入 Coze API Token！")
                    return
                if not new_config.get("coze_bot_id"):
                    QMessageBox.warning(self, "配置错误", "请输入 Bot ID！")
                    return
            elif bot_type == "openai":
                if not new_config.get("openai_api_key"):
                    QMessageBox.warning(self, "配置错误", "请输入 OpenAI API Key！")
                    return
            elif bot_type == "azure_openai":
                if not new_config.get("azure_openai_api_key"):
                    QMessageBox.warning(self, "配置错误", "请输入 Azure OpenAI API Key！")
                    return
                if not new_config.get("azure_openai_endpoint"):
                    QMessageBox.warning(self, "配置错误", "请输入 Azure OpenAI Endpoint！")
                    return
                if not new_config.get("azure_openai_deployment_name"):
                    QMessageBox.warning(self, "配置错误", "请输入 Azure OpenAI Deployment Name！")
                    return
            
            # 验证时间设置
            start_time = self.business_hours_card.start_time_picker.getTime()
            end_time = self.business_hours_card.end_time_picker.getTime()
            
            if start_time >= end_time:
                QMessageBox.warning(self, "时间设置错误", "开始时间必须早于结束时间！")
                return
            
            # 使用config模块保存配置
            config.update(new_config, save=True)
            
            self.logger.info("配置保存成功")
            
            # 显示成功消息
            InfoBar.success(
                title="保存成功",
                content="配置已保存！",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )
            
        except Exception as e:
            self.logger.error(f"保存配置失败: {e}")
            QMessageBox.critical(self, "保存失败", f"保存配置时发生错误：{str(e)}")
    
    def onResetConfig(self):
        """重置配置"""
        reply = QMessageBox.question(
            self,
            "确认重置",
            "确定要重置所有配置吗？\n这将重新加载配置文件中的原始设置。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # 使用config模块重新加载配置文件
                config.reload()
                self.loadConfig()
                self.logger.info("配置已重置")
                
                InfoBar.success(
                    title="重置成功",
                    content="配置已重置为配置文件中的设置！",
                    orient=Qt.Orientation.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self
                )
            except Exception as e:
                self.logger.error(f"重置配置失败: {e}")
                QMessageBox.critical(self, "重置失败", f"重置配置失败：{str(e)}")
    
 