import re
import idc
import ida_funcs

from get_call_arguments import get_call_arguments
from src.utils.get_heads_to_address import get_heads_to_address
from get_args_addresses import get_args_addresses
from src.utils.is_number import is_number


def is_argument(opnd, arguments):
    is_arg = False

    for arg in arguments:
        is_arg = is_arg or arg == opnd

    return is_arg


def is_overwritten(call, opnd):
    addresses = get_args_addresses(call)

    for address in addresses:
        if idc.GetOpnd(address, 0) == opnd:
            return True

    return False


def check_eax(addr, args):
    call_args = get_call_arguments(addr)
    is_arg = []

    for arg in call_args:
        is_arg.append(check_operand(arg, args, get_heads_to_address(addr)))

    for flag in is_arg:
        if flag:
            return True
    
    return False


def is_return_value(opnd):
    return re.match(r'r|e?ax', opnd) or opnd == 'al'


def check_next_opnd(head, call_arguments):
    opnd = idc.GetOpnd(head, 1)
    prev_head = idc.PrevHead(head)
    heads = get_heads_to_address(prev_head)

    return  check_operand(opnd, call_arguments, heads)


def check_operand(opnd, call_arguments, heads):
    if is_argument(opnd, call_arguments):
        return True

    for head in heads:
        if is_return_value(opnd) and idc.GetMnem(head) == 'call' and ida_funcs.func_does_return(head):
            return check_eax(head, call_arguments)

        if idc.GetMnem(head) == 'call' and is_overwritten(head, opnd):
            return False

        if opnd != idc.GetOpnd(head, 0):
            continue

        if not is_number(idc.GetOpnd(head, 1)) and check_next_opnd(head, call_arguments):
            return True

        if is_argument(opnd, call_arguments):
            return True

    return False


def is_argument_check(check_address, call):
    call_arguments = get_call_arguments(call)
    opnd1 = idc.GetOpnd(check_address, 0)
    opnd2 = idc.GetOpnd(check_address, 1)
    heads = get_heads_to_address(check_address)

    return check_operand(opnd1, call_arguments, heads) or check_operand(opnd2, call_arguments, heads)
