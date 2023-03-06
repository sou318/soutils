from decimal import Decimal as __Decimal


def add(base: list[int, float, __Decimal], calc: list[int, float, __Decimal]) -> list[int, float, __Decimal]:
    return [type(base[i])(__Decimal(str(base[i])) + __Decimal(str(calc[i]))) for i in range(len(base))]


def sub(base: list[int, float, __Decimal], calc: list[int, float, __Decimal]) -> list[int, float, __Decimal]:
    return [type(base[i])(__Decimal(str(base[i])) - __Decimal(str(calc[i]))) for i in range(len(base))]


def mul(base: list[int, float, __Decimal], calc: list[int, float, __Decimal]) -> list[int, float, __Decimal]:
    return [type(base[i])(__Decimal(str(base[i])) * __Decimal(str(calc[i]))) for i in range(len(base))]


def div(base: list[int, float, __Decimal], calc: list[int, float, __Decimal]) -> list[int, float, __Decimal]:
    return [type(base[i])(__Decimal(str(base[i])) / __Decimal(str(calc[i]))) for i in range(len(base))]
