import hashlib
import inspect
import time
from typing import Any, Callable, Tuple


def getRunTime(times: int = 1, output: bool = False) -> Callable:
    """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

    装饰后的函数将返回一个元组:(原函数返回值, 运行时长)
    运行时长: 类型int, 单位ns

    :param times: 运行次数, 默认为1
    :param output: 是否输出到流, 默认为False
    :return: 装饰后的函数
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
            if output:
                print(time_used)
            return fun_ret, time_used

        return runFun

    return ruturnFun


reRunTimes = getRunTime


def getFunName(fun: Callable) -> Callable:
    """函数形参增加__fun_name__用于获得函数名

    :param fun: 原函数
    :return: 装饰后的函数
    """
    name = fun.__name__

    def ret_fun(*args, **kwargs) -> Any:
        """装饰函数

        :return: 函数运算结果
        """
        return fun(*args, __fun_name__=name, **kwargs)

    return ret_fun


funName = getFunName


def isChange(
    hash: str = "0", ignore_line: int = 1, show_hash: bool = False
) -> Callable:
    """一个装饰器, 用来计算函数是否被修改

    :param hash: 预先计算的hash值, 默认为"0"
    :param ignore_line: 忽略函数的前几行不进行hash计算, 默认为1
    :param show_hash: 是否输出本次计算的hash值, 默认为False
    :return: 装饰后的函数
    """

    def ruturnFun(fun: Callable) -> Callable:
        """一个装饰器, 用来计算函数是否被修改

        :param fun: 原函数
        :return: 装饰器函数
        """

        def runFun(*args, **kwargs) -> tuple[Any, bool]:
            """一个装饰器, 用来计算函数是否被修改

            :return: 返回一个元组, 第一项为原返回值, 第二项是是否被修改, 被修改为True, 反之为False
            """
            is_change: bool = (
                False
                if (
                    ret_check_code := hashlib.sha224(
                        bytes(
                            "".join(
                                inspect.getsource(fun).split("\n")[ignore_line:]
                            ).encode("utf-8")
                        )
                    ).hexdigest()
                )
                == hash
                else True
            )  # 获取函数源码 去掉第一行装饰器 再获取hash 最后检查计算出来的hash和输入的hash是否一致
            if show_hash:
                print(ret_check_code)

            fun_ret = fun(*args, **kwargs)

            return fun_ret, is_change

        return runFun

    return ruturnFun
