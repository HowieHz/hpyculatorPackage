from queue import Queue
from typing import IO, Any

io_instance = None  # 我想用类属性的，但是时间给我干到原来的三倍，傻眼了
# 不加type hint的原因https://github.com/python/cpython/issues/79120
# https://stackoverflow.com/questions/60466092/why-does-order-of-declaration-matter-for-annotated-global-variables-in-modules

STRING = 1 << 0
NUM = 1 << 1
FLOAT = 1 << 2

ON = 1 << 1
OFF = 1 << 0  # 因为没读到就用这个作为缺省，所以每个参数的(1<<0)就是缺省

# 'output_mode'
RETURN_ONCE = 1 << 0
RETURN_ITERABLE = 1 << 1
# RETURN_ITERABLE_OUTPUT_IN_ONE_LINE = 1 << 2
NO_RETURN = 1 << 3
NO_RETURN_SINGLE_FUNCTION = 1 << 4

_message_queue: Queue = Queue()  # 输出消息 保证里面取出来的数据类型一定是str
# OutputReachedLimit
# CalculationProgramIsRunning
# CalculationProgramIsFinished（下一条消息是所用时间，类型int，单位ns）
# TypeConversionError
# CalculationError


def write(anything: Any, end: str = "\n") -> None:
    r"""用于向指定的文件流写入，每次写入之后立即刷新缓存区（立即写入硬盘）

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为"\n"
    """
    io_instance.write(str(anything) + end)  # type: ignore
    io_instance.flush()  # type: ignore


def write_without_flush(anything: Any, end: str = "\n") -> None:
    r"""用于向指定的文件流写入, 每次写入之后不刷新缓存区, 需要手动刷新(使用flush函数)

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为"\n"
    """
    io_instance.write(str(anything) + end)  # type: ignore


def flush() -> None:
    """用于刷新缓存区(将缓存区中的数据写入硬盘)"""
    io_instance.flush()  # type: ignore


def output(anything: Any) -> None:
    """输出到框体，会自动添加换行符

    :param anything: 要输出到框体的数据
    """
    if isinstance(anything, str):
        _message_queue.put(("OUTPUT", anything))
    else:
        _message_queue.put(("OUTPUT", str(anything)))


# 以下是用来传递数据的


def setIoInstance(instance: IO) -> None:
    """设置类属性: io实例

    :param instance: io实例
    """
    global io_instance
    io_instance = instance


def getIoInstance() -> IO:
    """返回io实例

    :return: io实例
    """
    return io_instance  # type: ignore  # 难以详细的标出IO类型
