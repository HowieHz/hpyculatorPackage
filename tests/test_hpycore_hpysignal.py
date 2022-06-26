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


@pytest.mark.run(order=1)
def test_hpysignal():
    """
    测试hpysignal子模块

    :return:
    """
    global test_reflect

    def _slot_fun(text: str):  # 模拟str型形参槽
        global test_reflect
        test_reflect = text

    def _slot_fun_none():  # 模拟无参数槽
        global test_reflect
        test_reflect = None

    def _slot_fun_bool(b: bool):  # 模拟bool型形参槽
        global test_reflect
        test_reflect = b

    # 绑定对应槽函数
    main_signal.set_output_box.connect(_slot_fun)
    main_signal.clear_output_box.connect(_slot_fun_none)
    main_signal.append_output_box.connect(_slot_fun)
    main_signal.insert_output_box.connect(_slot_fun)
    main_signal.append_output_box_.connect(_slot_fun)
    main_signal.insert_output_box_.connect(_slot_fun)
    main_signal.get_output_box.connect(_slot_fun_none)
    main_signal.set_start_button_text.connect(_slot_fun)
    main_signal.set_start_button_state.connect(_slot_fun_bool)
    main_signal.set_output_box_cursor.connect(_slot_fun)
    main_signal.draw_background.connect(_slot_fun_none)

    main_signal.set_output_box.emit(test_data)
    assert test_reflect == test_data

    main_signal.clear_output_box.emit()
    assert test_reflect is None

    main_signal.append_output_box.emit(test_data)
    assert test_reflect == test_data

    main_signal.insert_output_box.emit(test_data)
    assert test_reflect == test_data

    main_signal.append_output_box_.emit(test_data)
    assert test_reflect == test_data

    main_signal.insert_output_box_.emit(test_data)
    assert test_reflect == test_data

    main_signal.get_output_box.emit()
    assert test_reflect is None

    main_signal.set_start_button_text.emit(test_data)
    assert test_reflect == test_data

    main_signal.set_start_button_state.emit(test_bool)
    assert test_reflect == test_bool

    main_signal.set_output_box_cursor.emit(test_data)
    assert test_reflect == test_data

    main_signal.draw_background.emit()
    assert test_reflect is None


@pytest.mark.run(order=2)
def test_hpycore():
    """
    测试hpycore模块

    :return:
    """
    assert (num + 1) == hpycore.addOne(num)

    hpycore.setIoInstance(instance_io)
    assert instance_io == hpycore.getIoInstance()

    hpycore.setOutPutData(test_data)
    assert test_data == hpycore.getOutputData()

    hpycore.write(test_data, end="\n")
    assert test_reflect == f"{test_data}\n"

    hpycore.write_without_flush(test_data, end="\n")
    assert test_buffer == f"{test_data}\n"
    hpycore.flush()
    assert test_reflect == f"{test_data}\n"

    hpycore.setOutput(test_data)
    assert test_reflect == test_data

    hpycore.clearOutput()
    assert test_reflect is None

    hpycore.output_without_line_break(test_data)
    assert test_reflect == test_data
    hpycore.output_without_line_break(num)
    assert test_reflect == str_num

    hpycore.output(test_data)
    assert test_reflect == test_data
    hpycore.output(num)
    assert test_reflect == str_num
