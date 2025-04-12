while True:
    print('What to do?')
    print('\t1: Calculate BMI')
    print('\t2: Exit')
    
    user_choice = input('Select a number: ')
    
    if user_choice == '2':
        break
        # sys.exit(0)
    # import sys
    ''' Get user's height and weight '''
    ''' گرفتن قد و وزن کاربر '''    
    weight = input('Please enter your weight (kg): ')   
    height = input('Please enter your height (cm): ')
    
    weight = weight.strip()
    height = height.strip()
    
    ''' Check user's inputs '''
    # Error handling
    if weight.replace('.','',1).isdigit() and height.replace('.','',1).isdigit():
        ''' process inputs '''
        weight = float(weight)
        height = float(height)
        
        height = height / 100
        
        ''' Clculate BMI '''
        bmi = weight / height**2
        bmi_rounded = round(bmi, 2)
        
        ''' Check user status '''
        if bmi<18.5:
            status = 'Underweight'
        elif bmi>18.5 and bmi<25:
            status = 'Normal'
        else:
            status = 'Overweight'
        
        ''' Report to user '''
        print(f'Your BMI is {bmi:.2f} and your status is {status}')
    
    else:
        print('Please only enter numbers')

