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

    @hpydecorator.funName
    def _fun2(text: str, __fun_name__: str):
        return text, __fun_name__

    assert (test_data, "_fun2") == _fun2(test_data)
