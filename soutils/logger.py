from soutils import assets as __assets


def custom(values: list[object], msg: object) -> None:
    print(f"[{']['.join([str(value) for value in values])}] {str(msg)}")


def custom_set(kvset: dict) -> None:
    print("-"*32)
    keys: list[str] = [str(key) for key in list(kvset.keys())]
    space: int = max([len(key) for key in keys])
    for key in keys:
        print(key.ljust(space) + " : " + kvset[key])
    print("-"*32)


def template(values: list[object], type_: str, msg: object) -> None:
    output: list[str] = [
        __assets.now_time(),
        type_.center(4)
    ]
    output[1:1] = values
    custom(output, msg)


def template_set(kvset: dict) -> None:
    output: dict = {"Time": __assets.now_time()}
    output.update(kvset)
    custom_set(kvset)
