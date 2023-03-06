# ------------------------------------------------------------ #
from typing import Union as __Union
from soutils.types import string as __string


def is_number(num: str) -> bool:
    return __string.remove_chars((num[0].replace("-", "") + num[1:]), "0123456789.") == ""


def to_number(num: str) -> __Union[int, float]:
    return int(num) if int(num) == float(num) else float(num)
