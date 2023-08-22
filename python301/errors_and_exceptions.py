# from json.encoder import INFINITY
#
#
# try:
#     print('Trying 1/0')
#     total = 1 / 0
#     print('This will not show up')
# except ZeroDivisionError:
#     print('Exception was caught')
#     total = INFINITY
#
# print(total)
# print(type(total))

def getNum(prompt: str, default: float | None = None) -> float:
    if default is not None:
        prompt += f"[{default}]? "
    num = input(prompt)
    if default is not None and num == '':
        num = default
    try:
        num = float(num)
    except ValueError:
        print('That is not a number. Try again.')
        return getNum(prompt)
    return num
