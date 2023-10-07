from typing import TypeVar

Number = TypeVar('Number', int, float)

def add_one(number: Number) -> Number:
    return number + 1
