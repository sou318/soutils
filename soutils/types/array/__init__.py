from soutils.types.array import calc
from soutils.types.array import create
from soutils.types.array import type_
# ------------------------------------------------------------ #
from decimal import Decimal as __Decimal


def fibonacci(base: list[int, float, __Decimal], quantity: int) -> list[int, float]:
    result: list[__Decimal] = [__Decimal(str(i)) for i in base]
    for _ in range(quantity):
        result.append(sum(result[-len(base):]))
    return [int(result[i]) if float(result[i]).is_integer() else float(result[i]) for i in range(len(result))]


def remove_all(remove: list, value: object) -> list:
    for i in range(len(remove)):
        if remove[i] == value:
            del remove[i]
    return remove
