"""默认导入hpycore的所有属性和函数，易于使用"""
from .hpycore import (
    write,
    write_without_flush,
    flush,
    output,
    setIoInstance,
    getIoInstance,
    _message_queue,
    STRING,
    NUM,
    FLOAT,
    ON,
    OFF,
    RETURN_ONCE,
    RETURN_ITERABLE,
    NO_RETURN,
    NO_RETURN_SINGLE_FUNCTION,
)
from .hpysettings import SettingsFileObject

name = "hpyculator"
__all__ = ["hpy" + body for body in "core, decorator, settings, func".split(",")]
