from checks import get_cmp_addresses, get_test_addresses
from is_argument_check import is_argument_check


def is_checked(call_address):
    cmps = get_cmp_addresses(call_address)
    tests = get_test_addresses(call_address)

    for _cmp in cmps:
        if _cmp > call_address:
            continue

        if is_argument_check(_cmp, call_address):
            return True

    for test in tests:
        if test > call_address:
            continue

        if is_argument_check(test, call_address):
            return True

    return False
