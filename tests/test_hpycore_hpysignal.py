import tempfile
from random import randint
from typing import IO, Any, AnyStr

import pytest

# # 这样才可以导入上层包哈哈
# sys.path.append(os.path.join(sys.path[0], ".."))
from . import hpycore, main_signal

test_buffer: Any = 0  # 初始化一个变量，用于检测结果
test_reflect: Any = 0  # 初始化一个变量，用于检测结果


class io(IO):
    """模拟打开的文件流"""

    def __init__(self):
        ...

    def write(self, text: AnyStr) -> None:
        global test_buffer
        test_buffer = text

    def flush(self) -> None:
        global test_reflect
        test_reflect = test_buffer


instance_io = io()  # 创建实例

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
    assert (num + 1) == hpycore.addOne(num)

    hpycore.setIoInstance(instance_io)
    assert instance_io == hpycore.getIoInstance()

    hpycore.write(test_data, end="\n")
    assert test_reflect == f"{test_data}\n"

    hpycore.write_without_flush(test_data, end="\n")
    assert test_buffer == f"{test_data}\n"
    hpycore.flush()
    assert test_reflect == f"{test_data}\n"

    hpycore.output_without_line_break(test_data)
    assert test_reflect == test_data
    hpycore.output_without_line_break(num)
    assert test_reflect == str_num

    hpycore.output(test_data)
    assert test_reflect == test_data
    hpycore.output(num)
    assert test_reflect == str_num
