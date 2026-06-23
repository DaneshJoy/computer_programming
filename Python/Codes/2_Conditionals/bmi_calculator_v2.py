''' Get user's height and weight '''
weight = input('Please enter your weight (kg): ')
height = input('Please enter your height (cm): ')

# Type conversion
w = float(weight)
h = float(height)

''' Calculate BMI '''
bmi = w / (h/100) ** 2


''' Check User's Status '''
if bmi < 18.5:
    status = 'Underweight'
elif bmi <= 25:
    status = 'Normal'
else:  # bmi > 25
    status = 'Overweight'
    
# TODO: Add Obesity class checks to the above conditions


''' Report the result '''
bmi_rounded = round(bmi, 2)
print('BMI =', bmi_rounded)
print('Your status is', status)
