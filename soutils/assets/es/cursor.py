hidden = "\033[?25l"
display = "\033[?25h"


def up(n: int) -> str:
    return f"\033[{n}A"


def down(n: int) -> str:
    return f"\033[{n}B"


def right(n: int) -> str:
    return f"\033[{n}C"


def left(n: int) -> str:
    return f"\033[{n}D"
