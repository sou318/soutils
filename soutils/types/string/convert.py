def str2unicode(text: str) -> str:
    return "\\u" + ("\\u".join([hex(ord(i))[2:].rjust(4, "0") for i in text]))


def unicode2str(text: str) -> str:
    return "".join([chr(int(i, 16)) for i in text.split("\\u")[1:]])


def hyphen_upper(text: str) -> str:
    result: str = "".join([char.upper() if char.lower() == char else "-" + char.upper() for char in text])
    return result[1:] if text[0].upper() == text[0] else result


def hyphen_lower(text: str) -> str:
    result: str = "".join([char.lower() if char.lower() == char else "-" + char.lower() for char in text])
    return result[1:] if text[0].upper() == text[0] else result
