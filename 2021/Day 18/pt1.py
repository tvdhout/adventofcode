import re
import math

with open('input.txt') as file:
    numbers = file.read().split('\n')


def explode(number: str, position: int) -> str:
    left, pair, right = re.search(fr"(.{{{position}}})(\[\d+,\s*\d+])(.*)$", number).groups()
    left = re.sub(r"(\d+)([^\d]+)$",
                    lambda ex: f"{int(ex.group(1)) + eval(pair)[0]}{ex.group(2)}",
                    left)
    right = re.sub(r"^([^\d]+)(\d+)",
                    lambda ex: f"{ex.group(1)}{int(ex.group(2)) + eval(pair)[1]}",
                    right)
    return left+"0"+right


def split(number: str) -> str:
    nr = int(re.search(r"(\d\d+)", number)[0])
    left = nr // 2
    right = math.ceil(nr / 2)
    return re.sub(r"(\d\d+)", f"[{left},{right}]", number, count=1)


def reduce(number) -> str:
    nest = 0
    for position, char in enumerate(number):
        if char == '[':
            nest += 1
        elif char == ']':
            nest -= 1
        if nest > 4:
            number = reduce(explode(number, position))
            break
    else:
        if re.search(r"\d\d", number):
            number = reduce(split(number))
    return number


def magnitude(pair: list) -> int:
    left, right = pair
    left = 3 * (left if type(left) == int else magnitude(left))
    right = 2 * (right if type(right) == int else magnitude(right))
    return left + right


if __name__ == '__main__':
    reduction = numbers[0]
    for number in numbers[1:]:
        reduction = reduce(str([eval(reduction)] + [eval(number)]))
    print(reduction)
    print(magnitude(eval(reduction)))
