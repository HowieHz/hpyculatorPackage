# hpyculatorPackage

![PyPI - License](https://img.shields.io/pypi/l/hpyculator)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hpyculator)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f276a62341d647d08cd3c3dd275097ff)](https://www.codacy.com/gh/HowieHz/hpyculatorPackage/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=HowieHz/hpyculatorPackage&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/HowieHz/hpyculatorPackage/branch/main/graph/badge.svg?token=TVF40RMPMA)](https://codecov.io/gh/HowieHz/hpyculatorPackage)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hpyculator)
![GitHub repo size](https://img.shields.io/github/repo-size/HowieHz/hpyculatorPackage)

>基于python3.10

<https://github.com/HowieHz/hpyculator>

这个仓库是hpyculator的附属模块，如开发hpyculator插件需要此模块

## 安装方法

`pip install hpyculator`

## 子模块

### hpycore

    常量：
    STRING = 1 << 0
    NUM = 1 << 1
    FLOAT = 1 << 2
    LIST = 1 << 3
    
    ON = 1 << 1
    OFF = 1 << 0

    RETURN_ONCE = 1 << 0
    RETURN_ITERABLE = 1 << 1
    RETURN_ITERABLE_OUTPUT_IN_ONE_LINE = 1 << 2
    NO_RETURN = 1 << 3
    NO_RETURN_SINGLE_FUNCTION = 1 << 4

    函数
    def write(anything, end="\n") -> None:
    """
    用于向指定的文件流写入，每次写入之后立即刷新缓存区（立即写入硬盘）

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为换行符
    :return: None
    """

    def write_without_flush(anything, end="\n") -> None:
    """
    用于向指定的文件流写入，每次写入之后不刷新缓存区，需要手动刷新（使用flush函数）

    :param anything: 要写入的东西
    :param end: 每次写入在末尾追加的东西，默认为换行符
    :return: None
    """

    def flush() -> None:
    """
    用于刷新缓存区（将缓存区中的数据写入硬盘）

    :return: None
    """

    def output(anything) -> None:
    """
    输出到框体

    :param anything: 要输出到框体的数据
    :return: None
    """

细节请看文档<https://hpyculator.readthedocs.io/>

### hpydecorator

    实用装饰器
    
#### reRunTimes: 计量函数运行时间，并可以指定运行次数，
    
    def reRunTimes(times: int = 1) -> Callable:
    """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

    :param times: 运行次数, 默认为1
    :param output: 是否输出到流, 默认为False
    :return: 返回一个元组:(原函数调用结果, 总运行时长(ns为单位的))
    """

#### funName: 给原函数传入关键字参数__fun_name__，用于获取原函数名

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

#### isChange
    def isChange(hash: str = "0", ignore_line: int = 1, show_hash: bool = False)-> Callable:
    """
    一个装饰器, 用来计算函数是否被修改

    :param hash: 预先计算的hash值, 默认为"0"
    :param ignore_line: 忽略函数的前几行不进行hash计算, 默认为1
    :param show_hash: 是否输出本次计算的hash值, 默认为False
    """

### hpysettings

    用于快捷管理json，yaml，toml设置文件
    load函数用于创建一个设置文件对象（返回一个创建好的设置文件对象）
    设置文件对象的add，delete，modify方法支持链式调用

### hpyfunc

    def flatten(sequence: Union[list, tuple]) -> list:
    """
    将多维数据结构展平为一纬数据结构

    :param sequence:
    :return: list
    """
    
    def flatten_layer(sequence: Union[list, tuple]) -> list:
    """
    将多维数据结构展平一层

    :param sequence:
    :return: list
    """

    def flatten_no_recursion(sequence: Union[list, tuple]) -> list:
    """
    将多维数据结构展平为一纬数据结构（无递归） 效率低很多

    :param sequence:
    :return: list
    """
