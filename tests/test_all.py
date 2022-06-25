import tempfile
from typing import Any, AnyStr, IO

import pytest

# # 这样才可以导入上层包哈哈
# sys.path.append(os.path.join(sys.path[0], ".."))

from hpyc import hpycore, hpydecorator, hpyfunc
from hpyc.hpysignal import instance_main_win_signal as main_signal
from random import randint

test_buffer: Any = 0  # 初始化一个变量，用于检测结果
test_reflect: Any = 0  # 初始化一个变量，用于检测结果


class io(IO):
    def __init__(self):
        ...

    def write(self, text: AnyStr) -> None:
        global test_buffer
        test_buffer = text

    def flush(self) -> None:
        global test_reflect
        test_reflect = test_buffer


instance_io = io()

num = randint(0, 99999)
test_data = str(num) + "test_data"
test_bool = True


@pytest.mark.run(order=1)
def test_hpysignal():
    def _slot_fun(text: str):
        global test_reflect
        test_reflect = text

    def _slot_fun_none():
        global test_reflect
        test_reflect = None

    def _slot_fun_bool(b: bool):
        global test_reflect
        test_reflect = b

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

    hpycore.output(test_data)
    assert test_reflect == test_data


def test_hpydecorator():
    test_times: int = 0  # 初始化一个变量，用于检测结果

    @hpydecorator.reRunTimes(5)
    def _fun(text: str):
        nonlocal test_times
        test_times += 1
        return text

    ret = _fun(test_data)
    assert ret[0] == test_data and isinstance(ret[1], int)

    @hpydecorator.funName
    def _fun2(text: str, __fun_name__: str):
        return text, __fun_name__

    assert (test_data, "_fun2") == _fun2(test_data)


def test_hpyfunc():
    test_list = [1, 2, 3, [4, 5, [6, 7]]]
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten(test_list)
    assert [1, 2, 3, 4, 5, [6, 7]] == hpyfunc.flatten_layer(test_list)
    assert [1, 2, 3, 4, 5, 6, 7] == hpyfunc.flatten_no_recursion(test_list)
