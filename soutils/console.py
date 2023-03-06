import subprocess as __subprocess
import platform as __platform


def command(cmd: str) -> None:
    __subprocess.run(cmd, shell=True)


def printes(text: str) -> None:
    command("echo " + text)


def inputls(text: str) -> str:
    return input(text).lower().strip()


def over_print(text: str) -> None:
    printes(text="\033[1A\033[2K" + text)


def clear() -> None:
    command("cls" if __platform.system() == "Windows" else "clear")
