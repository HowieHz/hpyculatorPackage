import time
from typing import Callable, Tuple


def reRunTimes(times: int = 1) -> Callable:
    """
    一个装饰器，用来计算函数运行时长，这个函数是装饰器参数

    ---------------------------------------------

    返回一个元组：(原函数调用结果，ns为单位的运行时长)

    :param times: 运行次数，默认为1
    :return Tuple: 原函数调用结果，ns为单位的运行时长
    """

    def ruturnFun(fun: Callable) -> Callable:
        """nothing"""

        def runFun(*args, **kwargs) -> Tuple[Callable, int]:
            """nothing"""
            _time_start = time.perf_counter_ns()
            for _ in range(times):
                fun_ret = fun(*args, **kwargs)
            time_used = time.perf_counter_ns() - _time_start
            return fun_ret, time_used

        return runFun

    return ruturnFun


def funName(fun: Callable) -> Callable:
    """
    一个装饰器，函数形参增加__fun_name__用于获得函数名

    ---------------------------------------------

    使用方法：

    原函数
        def a(c, b: int = 1):

    ->

    改成
        def a(c, b: int = 1, __fun_name__):

    :param fun: 一个函数
    :return: 一个函数
    """
    name = fun.__name__

    def ret_fun(*args, **kwargs) -> Callable:
        """
        装饰器

        :param args: 参
        :param kwargs: 形参
        :return: 函数
        """
        return fun(*args, __fun_name__=name, **kwargs)

    return ret_fun
