from PySide6.QtCore import QObject, Signal


class MainWinSignal(QObject):
    """
    主窗口 自定义信号
    """

    set_output_box = Signal(str)
    clear_output_box = Signal()
    append_output_box = Signal(str)
    get_output_box = Signal()

    set_start_button_text = Signal(str)
    set_start_button_state = Signal(bool)

    set_output_box_cursor = Signal(str)


instance_main_win_signal = MainWinSignal()  # 单例模式
