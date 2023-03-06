import random as __random


def boolean() -> bool:
    return __random.choice([True, False])


def uuid() -> str:
    generate = "XXXXXXXX-XXXX-4XXX-XXXX-XXXXXXXXXXXX"
    resource = list("0123456789abcdef")
    for _ in range(generate.count("X")):
        generate = generate.replace("X", __random.choice(resource), 1)
    return generate
