from soutils.assets import es
# ------------------------------------------------------------ #
from datetime import datetime as __datetime


def now_time(file: bool = False) -> str:
    time = str(__datetime.now()).split(".")[0]
    if file:
        time = time.replace(":", "-").replace(" ", "_")
    return time
