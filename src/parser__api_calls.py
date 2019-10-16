import idaapi
import idautils
import idc


def get_start(address):
    print(address)
    return idaapi.get_func(int(address)).startEA


def get_end(address):
    return idaapi.get_func(int(address)).endEA


def get_function_address(head):
    return str(idc.get_operand_value(head, 0))


def get_jmp_functions(address):
    jmp_functions = []
    for head in idautils.Heads(get_start(address), get_end(address)):
        if idc.GetMnem(head) == 'call':
            jmp_functions.append(get_function_address(head))

    return jmp_functions


def get_api_calls(address):
    calls = []
    for function in get_jmp_functions(address):
        for head in idautils.Heads(get_start(function), get_end(function)):
            if idc.GetMnem(head) == 'jmp':
                calls.append(get_function_address(head))

    return calls
