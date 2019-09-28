import re

blackListFunctions = [
    r'^__',
    r'^sub_\d*',
]


def is_in_black_list(name):
    for reg in blackListFunctions:
        if re.match(reg, name):
            return True

    return False
