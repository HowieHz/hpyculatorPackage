from typing import IO, Any, Optional

from queue import Queue

io_instance: Optional[IO] = None  # 我想用类属性的，但是时间给我干到原来的三倍，傻眼了
output_data: Optional[str] = None  # 测试用的，获取输出框的数据

STRING = 1 << 0
NUM = 1 << 1
FLOAT = 1 << 2
LIST = 1 << 3

ON = 1 << 1
OFF = 1 << 0  # 因为没读到就用这个作为缺省，所以每个参数的(1<<0)就是缺省

# 'output_mode'
RETURN_ONCE = 1 << 0
RETURN_ITERABLE = 1 << 1
# RETURN_ITERABLE_OUTPUT_IN_ONE_LINE = 1 << 2
NO_RETURN = 1 << 3
NO_RETURN_SINGLE_FUNCTION = 1 << 4

message_queue = Queue()  # 输出消息 保证里面取出来的数据类型一定是str
# OutputReachedLimit
# CalculationProgramIsRunning
# CalculationProgramIsFinished（下一条消息是所用时间，类型int，单位ns）
output_queue = Queue()  # 输出结果 生产者-消费者模型 保证里面取出来的数据类型一定是str
error_queue = Queue()  # 输出错误 保证里面取出来的数据类型一定是str
# TypeConversionError
# CalculationError


def write(anything: Any, end: str = "\n") -> None:
    """
    用于向指定的文件流写入，每次写入之后立即刷新缓存区（立即写入硬盘）

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为"\n"
    """
    io_instance.write(str(anything) + end)
    io_instance.flush()


def write_without_flush(anything: Any, end: str = "\n") -> None:
    """用于向指定的文件流写入, 每次写入之后不刷新缓存区, 需要手动刷新(使用flush函数)

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为"\n"
    """
    io_instance.write(str(anything) + end)


def flush() -> None:
    """用于刷新缓存区(将缓存区中的数据写入硬盘)"""
    io_instance.flush()


def output(anything: Any) -> None:
    """输出到框体，会自动添加换行符

    :param anything: 要输出到框体的数据
    """
    if isinstance(anything, str):
        output_queue.put(anything)
    else:
        output_queue.put(str(anything))


def output_without_line_break(anything: Any) -> None:
    """输出到框体，但是不换行

    :param anything: 要输出到框体的数据
    """
    if isinstance(anything, str):  # 比直接str(anything)快
        output_queue.put(anything)
    else:
        output_queue.put(str(anything))


# 以下是用来传递数据的


def setIoInstance(instance: IO) -> None:
    """设置类属性: io实例

    :param instance: io实例
    """
    global io_instance
    io_instance: IO = instance


def getIoInstance() -> IO:
    """返回io实例

    :return: io实例
    """
    return io_instance


def setOutPutData(data: str) -> None:
    """设置output_data这个变量"""
    global output_data
    output_data = data


def addOne(num: int) -> int:
    """用于测试的函数，会输出输入数字+1的结果

    :param num: 一个数字
    :return: 输入+1
    """
    return num + 1
