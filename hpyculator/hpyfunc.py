from typing import Union, Callable, Optional
from array import ArrayType
import inspect


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


a_range_num = 10 * 50


def easy_text_hash(text: str) -> str:
    ret_num = 0
    for char in text:
        ret_num += ord(char) / 2
    if ret_num >= a_range_num:  # 控制在0-99999
        ret_num %= a_range_num  # 取末n位
    return str(int(ret_num))


def dont_change_my_code(
    fun: Callable,
    sign: str,
    hash_fun: Optional[Callable[[str], Union[int, str]]] = None,
    multisign: bool = False,
) -> str:
    """沙雕系列：别修改我的代码！
    使用print为计算出的hash值，未计算出结果则输出-1
    返回值也为计算出的hash值，未计算出结果则输出-1

    :param fun: 不要修改这个函数！
    :param sign: 标识符
    :param hash_fun: 你滴哈希函数，要求hash值范围在 0到(10 * 50 - 1)
    :param multisign: 允许多个标识符
    :return: hash值
    """
    if not hash_fun:
        hash_fun = easy_text_hash

    two_part_text = inspect.getsource(fun).split(sign)

    if len(two_part_text) < 2:
        raise TypeError("标识符应该至少出现一次！", f"实际出现了{len(two_part_text) - 1}次！")

    if len(two_part_text) != 2 and not multisign:
        raise TypeError("标识符应该只出现一次！", f"实际出现了{len(two_part_text)-1}次！")

    for num in range(a_range_num):
        if hash_fun(str(num).join(two_part_text)) == str(num):
            print(num)
            break
    else:
        print(-1)
    return str(num)
