import time
from typing import Any, Callable, Tuple


def reRunTimes(times: int = 1) -> Callable:
    """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

    :param times: 运行次数, 默认为1
    :return: 装饰器函数
    """

    def ruturnFun(fun: Callable) -> Callable:
        """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

        :param fun: 原函数
        :return: 装饰器函数
        """

        def runFun(*args, **kwargs) -> Tuple[Any, int]:
            """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

            :return: 返回一个元组:(原函数调用结果, ns为单位的运行时长)
            """
            _time_start = time.perf_counter_ns()
            for _ in range(times):
                fun_ret = fun(*args, **kwargs)
            time_used = time.perf_counter_ns() - _time_start
            return fun_ret, time_used

        return runFun

    return ruturnFun


def funName(fun: Callable) -> Callable:
    """一个装饰器, 函数形参增加__fun_name__用于获得函数名
    ---------------------------------------------

    使用方法:

    原函数
        def a(c, b: int = 1):

    ->

    改成
        def a(c, b: int = 1, __fun_name__):


    :param fun: 原函数
    :return: 装饰器函数
    """
    name = fun.__name__

    def ret_fun(*args, **kwargs) -> Any:
        """装饰函数

        :return: 函数运算结果
        """
        return fun(*args, __fun_name__=name, **kwargs)

    return ret_fun
