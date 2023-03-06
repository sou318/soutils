from soutils.assets import es
# ------------------------------------------------------------ #
from datetime import datetime as __datetime


def now_time() -> str:
    return str(__datetime.now()).split(".")[0]
