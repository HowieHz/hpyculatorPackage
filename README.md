# hpyculatorPackage

![PyPI - License](https://img.shields.io/pypi/l/hpyculator)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hpyculator)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f276a62341d647d08cd3c3dd275097ff)](https://www.codacy.com/gh/HowieHz/hpyculatorPackage/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=HowieHz/hpyculatorPackage&amp;utm_campaign=Badge_Grade)
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
        reRunTimes: 计量函数运行时间，并可以指定运行次数，如要运行5次 @reRunTimes(5)，返回值变为(原返回值，运行时间(单位ns))
        def reRunTimes(times: int = 1) -> Callable:
        """
        一个装饰器，用来计算函数运行时长，这个函数是装饰器参数
        
        ---------------------------------------------
        
        返回一个元组：(原函数调用结果，ns为单位的运行时长)
        
        :param times: 运行次数，默认为1
        :return Tuple: 原函数调用结果，ns为单位的运行时长
        """       

        funName: 给原函数传入关键字参数__fun_name__，用于获取原函数名
        funName(fun: Callable) -> Callable:
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

### hpysettings

    用于快捷管理json，yaml，toml设置文件
    load函数用于创建一个设置文件对象（返回一个创建好的设置文件对象）
    设置文件对象的add，delete，modify方法支持链式调用

### hpysignal

    instance_main_win_signal用于操作主窗口
        set_output_box设置输出窗口文字，传入一个参数(str)
        clear_output_box清空输出窗口文字
        append_output_box追加输出窗口文字，传入一个参数(str)

        set_start_button_text设置开始按钮上的文字，传入一个参数(str)
        set_start_button_state设置开始按钮是否启用，传入一个参数(bool)

        set_output_box_cursor设置输出窗口的指针位置，传入一个参数(str)

    使用方法：
        instance_main_win_signal.clear_output_box.emit()
        instance_main_win_signal.set_output_box.emit("text")

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

[//]: # ()
[//]: # (## 更多细节请看文档)

[//]: # ()
[//]: # (<https://hpyculator.readthedocs.io/>)
