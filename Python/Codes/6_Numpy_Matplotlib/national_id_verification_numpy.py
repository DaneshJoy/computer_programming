# https://camelcase.ir/الگوریتم-اعتبارسنجی-کدملی/
# https://majidh1.github.io/iranianNationalCode/

import numpy as np


codes = ['0939685736', '939685736', '1234567890', '1111111111']
# عبدالرضا سلمانیان قهدریجانی

def validate_national_id(code):
    if len(code)<8 or len(code)>10:
        return False
    
    if len(set(code)) == 1:
        return False
    
    code = code.zfill(10)
    
    coefs = np.flip(np.arange(2, 11))
    # coefs = np.arange(2, 11)[::-1]

    numbers = np.array(list(code)[:-1], dtype=int)
    
    checksum = np.dot(coefs, numbers)
    # checksum = coefs @ numbers
    
    remainder = checksum % 11
    control_digit = remainder if remainder<2 else 11 - remainder
    
    if control_digit != int(code[-1]):
        return False
    
    return True


for code in codes:
    if validate_national_id(code):
        status = "Valid"
    else:
        status = 'Invalid'
    print(f'{code} is {status}')
    