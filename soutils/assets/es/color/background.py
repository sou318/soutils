black = "\033[40m"
red = "\033[41m"
green = "\033[42m"
yellow = "\033[43m"
blue = "\033[44m"
magenta = "\033[45m"
cyan = "\033[46m"
white = "\033[47m"
reset = "\033[49m"


def rgb(r: int, g: int, b: int) -> str:
    return f"\033[48;2;{r};{g};{b}m"
