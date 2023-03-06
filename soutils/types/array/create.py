from typing import Union as __Union


def range_hex(quantity: __Union[int, hex]) -> list[hex]:
    if type(quantity) == int:
        return [hex(i) for i in range(quantity)]
    elif type(quantity) == hex:
        return [hex(i) for i in range(int(str(quantity), 16))]
