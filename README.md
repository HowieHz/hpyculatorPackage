# hpyculatorPackage

>基于python3.10

<https://github.com/HowieHz/hpyculator>

这个仓库是hpyculator的附属模块，如开发hpyculator插件需要此模块

## 安装方法

`pip install hpyculator`

## 子模块(方法注释完备，以方法注释为准)

### hpycore

    内有若干常量和函数

细节请看文档<https://hpyculator.readthedocs.io/>

### hpydecorator

    实用装饰器
        reRunTimes: 计量函数运行时间，并可以指定运行次数，如要运行5次 @reRunTimes(5)，返回值变为(原返回值，运行时间(单位ns))
        funName: 给原函数传入关键字参数__fun_name__，用于获取原函数名

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

## 更多细节请看文档

<https://hpyculator.readthedocs.io/>
