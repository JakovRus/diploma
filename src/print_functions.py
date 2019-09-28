from idautils import *
from idc import *
from functions_utils import *

addresses = get_user_functions()

for address in addresses:
    if is_user_function(address):
        print GetFunctionName(address)
