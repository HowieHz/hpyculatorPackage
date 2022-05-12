from PySide6.QtCore import QObject, Signal


class MainWindowSignal(QObject):
    """
    主窗口 自定义信号
    """

    setOutPutBox = Signal(str)
    clearOutPutBox = Signal()
    appendOutPutBox = Signal(str)
    getOutPutBox = Signal()

    setStartButtonText = Signal(str)
    setStartButtonState = Signal(bool)

    setOutPutBoxCursor = Signal(str)


class SettingWindowSignal(QObject):
    """
    设置窗口 自定义信号
    """


main_window_signal = MainWindowSignal()
setting_window_signal = SettingWindowSignal()
