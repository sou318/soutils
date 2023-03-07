# ------------------------------------------------------------ #
from typing import Union as __Union


def get_key_data_list(dictionary: dict, key: object) -> list[object]:
    return [dictionary[k][key] for k in list(dictionary.keys())]


def reverse_lookup(dictionary: dict, value: object) -> list[str]:
    return_data: list = []
    for key in list(dictionary.keys()):
        if dictionary[key] == value:
            return_data.append(key)
    return return_data


def remove_value_match_element(dictionary: dict, value: __Union[list, object]) -> dict:
    for key in list(dictionary.keys()):
        if type(value) == list:
            result: dict = dictionary
            for data in value:
                result = remove_value_match_element(result, data)
        else:
            if dictionary[key] == value:
                del dictionary[key]
    return dictionary


def sort_key(dictionary: dict, reverse: bool = False) -> dict:
    return dict(sorted(dictionary.items(), reverse=reverse))


def sort_value(dictionary: dict, reverse: bool = False) -> dict:
    return dict(sorted(dictionary.items(), reverse=reverse, key=lambda x: x[1]))
