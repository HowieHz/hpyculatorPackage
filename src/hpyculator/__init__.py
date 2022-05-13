"""
基本属性
"""
from .hpycore import *

name = "hpyculator"
__all__ = ["hpy" + body for body in "core,signal,decorator,setting".split(",")]
__version__ = "1.4.6"
