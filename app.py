import sys
import ctypes
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from utils.logger import get_logger

def main():
    """ 应用程序主函数 """
    # 启用高分屏支持 - 必须在创建QApplication之前设置
    if hasattr(Qt.ApplicationAttribute, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    if hasattr(Qt.ApplicationAttribute, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)

    # 创建QApplication实例 - 必须在任何QWidget创建之前
    app = QApplication(sys.argv)
    
    # 初始化logger - 在QApplication创建之后
    logger = get_logger("App")
    logger.info("应用程序启动...")
    
    # 在Windows上设置AppUserModelID，以确保任务栏图标正确显示
    try:
        if sys.platform == "win32":
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my.company.my.product.version")
    except Exception as e:
        logger.warning(f"设置AppUserModelID失败: {e}")

    # Import MainWindow after QApplication is created to avoid "Must construct a QApplication before a QWidget" error
    from ui.main_ui import MainWindow

    # 初始化并显示主窗口
    window = MainWindow()
    window.show()

    # 运行事件循环
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
