from soutils import assets as __assets
from typing import Union as __Union
import os as __os

split: str = "-" * 32
log_dir: str = "./log/"
log_file: str = __assets.now_time(True) + ".log"
log_list: list[str] = []
ljust_user: int = 20
ljust_type: int = 5
type_upper: bool = True


def init() -> None:
    if not __os.path.exists(log_dir):
        __os.mkdir(log_dir)
    with open(log_dir + log_file, "w", encoding="UTF-8"):
        pass


def write() -> None:
    global log_list
    output: str = "\n".join(log_list)
    print(output)
    with open(log_dir + log_file, "a", encoding="UTF-8") as WriteFile:
        WriteFile.write(output + "\n")
    log_list = []


def free(msg: str) -> None:
    log_list.append(msg)


def template(user: __Union[int, str, None], msg: str, log_type: str) -> None:
    if type_upper:
        log_type = log_type.upper()
    output: str = "][".join([
        __assets.now_time(),
        str(user).ljust(ljust_user),
        log_type.ljust(ljust_type)
    ])
    free("[" + output + "] " + msg)


def log(user: __Union[int, str, None], msg: str) -> None:
    template(user, msg, "LOG")


def error(user: __Union[int, str, None], msg: str) -> None:
    template(user, msg, "ERROR")


def warning(user: __Union[int, str, None], msg: str) -> None:
    template(user, msg, "WARN")


def info(user: __Union[int, str, None], msg: str) -> None:
    template(user, msg, "INFO")
