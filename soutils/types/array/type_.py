def same(array: list, same_type: type) -> bool:
    return [type(i) for i in array].count(same_type) == len(array)


def convert(array: list, convert_type: type) -> list[object]:
    return [convert_type(i) for i in array]
