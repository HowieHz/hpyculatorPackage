from random import randint

from . import hpydecorator

# 测试数据
num = randint(0, 99999)
test_data = str(num) + "test_data"


def test_hpydecorator():
    test_times: int = 0  # 初始化一个变量，用于检测结果

    @hpydecorator.reRunTimes(5)
    def _fun(text: str):
        nonlocal test_times
        test_times += 1
        return text

    ret = _fun(test_data)
    assert ret[0] == test_data and isinstance(ret[1], int)

    @hpydecorator.reRunTimes(
        5,
    )
    def _fun(text: str):
        nonlocal test_times
        test_times += 1
        return text

    ret = _fun(test_data)

    @hpydecorator.funName
    def _fun2(text: str, __fun_name__: str):
        return text, __fun_name__

    assert (test_data, "_fun2") == _fun2(test_data)

    @hpydecorator.isChange(
        hash="0",
        ignore_line=4,
        show_hash=True,
    )
    def _fun3() -> None:
        """func

        :return: None
        """
        print("hello")

    assert _fun3()[1] is True  # 代码被修改

    @hpydecorator.isChange(
        hash="b43a3a7707a994190404a6d10a43cb2bae695289e158560f9a4f89c4",
        ignore_line=4,
        show_hash=False,
    )
    def _fun4() -> None:
        """func

        :return: None
        """
        print("hello")

    assert _fun4()[1] is True  # 代码未被修改
