import idaapi
import idautils
import idc


def get_api_calls(address):
    calls = []
    func = idaapi.get_func(address)
    for head in idautils.Heads(func.startEA, func.endEA):
        mnem = idc.GetMnem(head)
        if mnem == 'call':
            print calls.append(str(head) + ':' + idc.GetMnem(head) + ' ' + idc.GetOpnd(head, 0))

    return calls
