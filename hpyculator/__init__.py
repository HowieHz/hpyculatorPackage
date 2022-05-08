from .signal import main_window_signal
from .signal import setting_window_signal

name = "hpyculator"

def write(io_instance,anything,end="\n") -> None:
    """
    用于向指定的文件流写入，每次写入之后立即刷新缓存区（立即写入硬盘）

    :param io_instance: 打开的可写文件流对象
    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为换行符
    :return: None
    """
    io_instance.write(str(anything)+end)
    io_instance.flush()

def write_without_flush(io_instance,anything,end="\n") -> None:
    """
    用于向指定的文件流写入，每次写入之后不刷新缓存区，需要手动刷新（使用flush函数）

    :param io_instance: 打开的可写文件流对象
    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为换行符
    :return: None
    """
    io_instance.write(str(anything)+end)

def flush(io_instance) -> None:
    """
    用于刷新缓存区（将缓存区中的数据写入硬盘）

    :param io_instance: 打开的可写文件流对象
    :return: None
    """
    io_instance.flush()

def output(anything) -> None:
    """
    输出到框体

    :param anything: 要输出到框体的数据
    :return: None
    """
    main_window_signal.appendOutPutBox.emit(str(anything))

def clearOutput() -> None:
    """
    清空输出框

    :return: None
    """
    main_window_signal.clearOutPutBox.emit()

def setOutput(msg:str) -> None:
    """
    设置输出框的显示数据

    :param msg: 要输出到框体的数据
    :return: None
    """
    main_window_signal.setOutPutBox.emit(msg)

def addOne(num:int) -> int:
    """
    用于测试的函数，会输出输入数字+1的结果

    :param num: 一个数字
    :return: int
    """
    return num+1

STRING=(1<<0)
NUM=(1<<1)
FLOAT=(1<<2)
LIST=(1<<3)

ON=(1<<1)
OFF=(1<<0)#因为没读到就用这个作为缺省，所以每个参数的(1<<0)就是缺省

#'output_mode'
RETURN_ONCE=(1<<0)
RETURN_LIST=(1<<1)
RETURN_LIST_OUTPUT_IN_ONE_LINE=(1<<2)
NO_RETURN=(1<<3)
NO_RETURN_SINGLE_FUNCTION=(1<<4)