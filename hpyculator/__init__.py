"""默认导入hpycore的所有属性和函数，易于使用"""
from .hpycore import (
    FLOAT,
    NO_RETURN,
    NO_RETURN_SINGLE_FUNCTION,
    NUM,
    OFF,
    ON,
    RETURN_ITERABLE,
    RETURN_ONCE,
    STRING,
    _message_queue,
    flush,
    getIoInstance,
    output,
    setIoInstance,
    write,
    write_without_flush,
)
from .hpysettings import SettingsFileObject

name = "hpyculator"
__all__ = ["hpy" + body for body in "core, decorator, settings, func".split(",")]
