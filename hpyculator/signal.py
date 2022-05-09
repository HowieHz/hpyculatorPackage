from PySide6.QtCore import Signal, QObject


class MainWindowSignal(QObject):
    setOutPutBox = Signal(str)
    clearOutPutBox = Signal()
    appendOutPutBox = Signal(str)

    setStartButtonText = Signal(str)
    setStartButtonState = Signal(bool)

class SettingWindowSignal(QObject):
    pass

main_window_signal = MainWindowSignal()
setting_window_signal = SettingWindowSignal()
