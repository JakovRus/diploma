import sys
import os

sys.path.append(os.getcwd())

import idc

from src.code_parser.user_functions import get_user_functions
from src.missing_checks.get_missing_checks import get_missing_checks
from src.utils.get_function_address import get_function_address


def find_missing_checks():
    idc.auto_wait()

    addresses = get_user_functions()

    for address in addresses:
        calls = get_missing_checks(address)

        if len(calls):
            print('*******************')
            print(idc.get_func_name(int(address)) + ':' + str(address))
            print('------------------')

        for call in calls:
            function_address = get_function_address(call)
            print(idc.get_func_name(int(function_address)) + ':' + str(function_address))

        if len(calls):
            print('*******************')


find_missing_checks()
# idc.Exit(0)


# *******************
# ?copyTo10@@YAXPEAD0@Z:5368783760
# ------------------
# ?customStrcpy@@YAXPEAD0@Z:5368783872
# *******************
