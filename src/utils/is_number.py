import re


def is_number(_str):
    _str = re.sub('h$', '', _str)

    try:
        int(_str, 16)
        return True
    except ValueError:
        return False
