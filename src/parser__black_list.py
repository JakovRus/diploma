import re

blackListFunctions = [
    r'^\?__empty_global_delete',
    r'^\?_RTC_',
    r'.*__RTC_.*',
    r'.*std.*',
    r'^\?__scrt_',
    r'.*CheckForDebuggerJustMyCode.*',
]


def is_in_black_list(name):
    for reg in blackListFunctions:
        if re.match(reg, name):
            return True

    return False
