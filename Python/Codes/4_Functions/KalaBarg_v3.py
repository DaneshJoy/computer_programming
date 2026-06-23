from persiantools.jdatetime import JalaliDateTime
from national_id_verification import validate_national_id


while True:
    ''' Get user's National ID (Code Melli) '''
    melli_code = input('Please enter your National ID: ')
    
    # Validate National ID
    code, status = validate_national_id(melli_code)
    
    if status == 'Invalid':
        print('National ID is Invalid')
        continue
        
    ''' Get Todays Day of Month '''
    today = JalaliDateTime.now().day
    
    
    ''' Check if User's KalaBarg is Charged or Not '''
    last_digit = melli_code[-1]
    
    # Method 1
    status = 'Not Charged'
    if last_digit in ['0', '1', '2']:
        if today >= 15:
            status = 'Charged'
    elif last_digit in ['3', '4', '5']:
        if today >= 20:
            status = 'Charged'
    else:
        if today >= 25:
            status = 'Charged'
            
    print(status)
    
    cnt = input('Continue (y/n)?: ')
    if cnt != 'y':
        break

