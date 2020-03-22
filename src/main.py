import sys
import os

from src.code_parser.api_calls import get_api_calls
from src.function_parser.get_calls_addresses import get_calls_addresses
from src.missing_checks.get_checked_calls import get_checked_calls

sys.path.append(os.getcwd())

import idc
import datetime

from src.code_parser.user_functions import get_user_functions
from src.missing_checks.get_missing_checks import get_missing_checks
from src.utils.get_function_address import get_function_address


def find_missing_checks():
    idc.auto_wait()

    addresses = get_user_functions()
    checked_calls = {}
    calls_addresses = {}

    for address in addresses:
        func_calls_addresses = get_calls_addresses(address)
        checked_calls[address] = get_checked_calls(func_calls_addresses)
        calls_addresses[address] = func_calls_addresses

    current_date = datetime.datetime.now()
    print ('[2]', str(current_date))
    for address in addresses:
        calls = get_missing_checks(address, checked_calls, calls_addresses)

        if len(calls):
            print('*******************')
            print(idc.get_func_name(int(address)) + ':' + str(address))
            print('------------------')

        for call in calls:
            function_address = get_function_address(call)
            print(idc.get_func_name(int(function_address)) + ':' + str(function_address))

        if len(calls):
            print('*******************')


currentDT = datetime.datetime.now()
print ('[1]', str(currentDT))
find_missing_checks()
currentDT = datetime.datetime.now()
print ('[3]', str(currentDT))
# idc.Exit(0)


# *******************
# ?copyTo10@@YAXPEAD0@Z:5368783760
# ------------------
# ?customStrcpy@@YAXPEAD0@Z:5368783872
# *******************
