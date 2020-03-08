import idc


def get_function_address(head):
    return str(idc.get_operand_value(head, 0))