"""默认导入hpycore的所有属性和函数，易于使用"""
from .hpycore import *
from .hpysettings import SettingsFileObject

name = "hpyculator"
__all__ = ["hpy" + body for body in "core, decorator, settings, func".split(",")]
