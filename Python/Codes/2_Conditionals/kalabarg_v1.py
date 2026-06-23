from datetime import datetime


''' Get user's National ID (Code Melli) '''
melli_code = input('Please enter your National ID: ')


''' Get Todays Day of Month '''
# today = datetime.now().day
today = 16


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
    

