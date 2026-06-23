def validate_national_id(code):
    if len(code) < 8 or len(code) > 10:
        status = 'Invalid'
        return status
    else:
        code = code.zfill(10)
    
    place_digits = list(range(2, 11))
    place_digits.reverse()
    
    checksum = 0
    for i in range(len(place_digits)):
        checksum += int(code[i])*place_digits[i]
    
    remainder = checksum % 11
    
    if remainder < 2:
        control_digit = remainder
    else:
        control_digit = 11 - remainder
        
    if control_digit == int(code[-1]):
        status = 'Valid'
    else:
        status = 'Invalid'
    
    return code, status    