from .signal import main_window_signal


class Main():
    def __init__(self):
        self.io_instance: open = None
        self.STRING = (1 << 0)
        self.NUM = (1 << 1)
        self.FLOAT = (1 << 2)
        self.LIST = (1 << 3)

        self.ON = (1 << 1)
        self.OFF = (1 << 0)  # 因为没读到就用这个作为缺省，所以每个参数的(1<<0)就是缺省

        # 'output_mode'
        self.RETURN_ONCE = (1 << 0)
        self.RETURN_LIST = (1 << 1)
        self.RETURN_LIST_OUTPUT_IN_ONE_LINE = (1 << 2)
        self.NO_RETURN = (1 << 3)
        self.NO_RETURN_SINGLE_FUNCTION = (1 << 4)

    def write(self,anything, end="\n") -> None:
        """
        用于向指定的文件流写入，每次写入之后立即刷新缓存区（立即写入硬盘）

        :param io_instance: 打开的可写文件流对象
        :param anything: 要写入的东西
        :param end: 每次写入在末尾追加的东西，默认为换行符
        :return: None
        """
        self.io_instance.write(str(anything) + end)
        self.io_instance.flush()
        return None

    def write_without_flush(self,anything, end="\n") -> None:
        """
        用于向指定的文件流写入，每次写入之后不刷新缓存区，需要手动刷新（使用flush函数）

        :param io_instance: 打开的可写文件流对象
        :param anything: 要写入的东西
        :param end: 每次写入在末尾追加的东西，默认为换行符
        :return: None
        """
        self.io_instance.write(str(anything) + end)
        return None

    def flush(self) -> None:
        """
        用于刷新缓存区（将缓存区中的数据写入硬盘）

        :param io_instance: 打开的可写文件流对象
        :return: None
        """
        self.io_instance.flush()
        return None

    def output(self,anything) -> None:
        """
        输出到框体

        :param anything: 要输出到框体的数据
        :return: None
        """
        main_window_signal.appendOutPutBox.emit(str(anything))
        return None

    def clearOutput(self) -> None:
        """
        清空输出框

        :return: None
        """
        main_window_signal.clearOutPutBox.emit()
        return None

    def setOutput(self,msg: str) -> None:
        """
        设置输出框的显示数据

        :param msg: 要输出到框体的数据
        :return: None
        """
        main_window_signal.setOutPutBox.emit(msg)
        return None

    def addOne(self,num: int) -> int:
        """
        用于测试的函数，会输出输入数字+1的结果

        :param num: 一个数字
        :return: int
        """
        return num + 1

    def setIoInstance(self,io_instance) -> None:
        """
        设置类属性：io实例

        :param io_instance: io实例
        :return: None
        """
        self.io_instance = io_instance
        return None

    def getIoInstance(self):
        """
        返回io实例

        :return: 类属性：io实例
        """
        return self.io_instance