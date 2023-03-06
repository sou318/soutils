from soutils.types.string import convert
# ------------------------------------------------------------ #
from typing import Union as __Union


def dictionary_replace(text: str, dictionary: dict, reverse: bool = False) -> str:
    if not reverse:
        for key in list(dictionary.keys()):
            text = text.replace(key, dictionary[key])
    else:
        keys: list[str] = list(dictionary.keys())
        for i in range(len(keys)):
            key: str = keys[-i - 1]
            text = text.replace(dictionary[key], key)
    return text


def remove_chars(text: str, chars: __Union[str, list[str]]) -> str:
    for char in list(chars):
        text = text.replace(str(char), "")
    return text
