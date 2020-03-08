from get_cmp_addresses import get_cmp_addresses
from is_argument_check import is_argument_check


def is_checked(call_address):
    checks = get_cmp_addresses(call_address)

    for _cmp in checks:
        if is_argument_check(_cmp, call_address):
            return True

    return False
