from typing import Union


def flatten(sequence: Union[list, tuple]) -> list:
    """将多维数据结构展平为一纬数据结构

    :param sequence: 多维数据结构
    :return: 一纬数据结构
    """
    ret = []
    for _ in sequence:
        if isinstance(_, list):
            ret.extend(flatten(_))
        else:
            ret.append(_)
    return ret


def flatten_layer(sequence: Union[list, tuple]) -> list:
    """将多维数据结构展平一层

    :param sequence: 多维数据结构
    :return: 展平了一层的一纬数据结构
    """
    ret = []
    for _ in sequence:
        if isinstance(_, list):
            ret.extend(_)
        else:
            ret.append(_)
    return ret


def flatten_no_recursion(sequence: Union[list, tuple]) -> list:
    """将多维数据结构展平为一纬数据结构(无递归)效率低很多

    :param sequence: 多维数据结构
    :return: 一纬数据结构
    """
    while True:
        if all(not isinstance(_, list) for _ in sequence):  # 全不是列表
            return sequence
        sequence = flatten_layer(sequence)
