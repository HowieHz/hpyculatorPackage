from random import randint
from typing import IO, Any, AnyStr

# # 这样才可以导入上层包哈哈
# sys.path.append(os.path.join(sys.path[0], ".."))
from . import _message_queue, hpycore

test_buffer: Any = 0  # 初始化一个变量，用于检测结果
test_reflect: Any = 0  # 初始化一个变量，用于检测结果


class io(IO):
    """模拟打开的文件流"""

    def __init__(self):
        ...

    def write(self, text: AnyStr) -> None:  # type: ignore
        global test_buffer
        test_buffer = text

    def flush(self) -> None:
        global test_reflect
        test_reflect = test_buffer


instance_io = io()  # type: ignore # 创建实例 __enter__和__exit__方法测试用不到就算了

# 测试数据
num = randint(0, 99999)
str_num = str(num)
test_data = str(num) + "test_data"
test_bool = True


def test_hpycore():
    """
    测试hpycore模块

    :return:
    """

    hpycore.setIoInstance(instance_io)
    assert instance_io == hpycore.getIoInstance()

    hpycore.write(test_data, end="\n")
    assert test_reflect == f"{test_data}\n"

    hpycore.write_without_flush(test_data, end="\n")
    assert test_buffer == f"{test_data}\n"
    hpycore.flush()
    assert test_reflect == f"{test_data}\n"

    hpycore.output(test_data)
    assert _message_queue.get() == test_data
    hpycore.output(num)
    assert _message_queue.get() == str_num
