phone_number = "09915648345"

first_4_digits = phone_number[:4]
last_3_numbers = int(phone_number[-3:])
stars = '***'

# Concatenation
# winner = first_4_digits + stars + last_3_numbers

print('The winner is: ', first_4_digits, stars, last_3_numbers, sep='')
