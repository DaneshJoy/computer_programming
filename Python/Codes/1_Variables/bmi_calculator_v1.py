''' Get user's height and weight '''
weight = input('Please enter your weight (kg): ')
height = input('Please enter your height (cm): ')

# Type conversion
w = float(weight)
h = float(height)

''' Calculate BMI '''
bmi = w / (h/100) ** 2

''' Report the result '''
bmi_rounded = round(bmi, 2)
print('BMI =', bmi_rounded)
