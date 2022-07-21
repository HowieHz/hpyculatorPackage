from typing import Union
from array import ArrayType


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

    # [(flatten(_) if isinstance(_, list) else _) for _ in sequence]
    return ret


def flatten_layer(sequence: Union[list, tuple]) -> list:
    """将多维数据结构展平一层

    :param sequence: 多维数据结构
    :return: 展平了一层的一纬数据结构
    """
    ret = []
    for _ in sequence:
        ret.extend(_ if isinstance(_, list) else [_])
    return ret


def flatten_no_recursion(sequence: Union[list, tuple]) -> Union[list, tuple]:
    """将多维数据结构展平为一纬数据结构(无递归)

    :param sequence: 多维数据结构
    :return: 一纬数据结构
    """
    while True:
        if all(not isinstance(_, list) for _ in sequence):  # 全不是列表
            return sequence
        sequence = flatten_layer(sequence)


def expand_dims(
    array: Union[ArrayType, list], *dims, padding_value: Union[str, int, float] = 0
):
    """将一纬数据结构提升至多维

    :param array: 一维列表/数组
    :param dims: 各项维度上限 (顺序从最里层向外)
    :param padding_value: 填充值 默认为0
    """
    allLen: int = 1  # 总长
    for num in dims:
        allLen *= num
    if len(array) < allLen:  # 补齐长度
        array.extend([padding_value for _ in range(allLen - len(array))])

    for n in dims:
        array = [array[i : i + n] for i in range(0, len(array), n)]
    return array[0]
