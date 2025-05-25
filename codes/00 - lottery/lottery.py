import random

# Create a list of numbers
phone_numbers = []
pre = "09"
for i in range(10):
    numbers = random.randint(100_000_000, 999_999_999)
    phone_number = f'{pre}{numbers}'
    phone_numbers.append(phone_number)

winner = random.choice(phone_numbers)

first_4_digits = winner[:4]
last_3_numbers = int(winner[-3:])
stars = '***'

# Concatenation
# winner = first_4_digits + stars + last_3_numbers

print('The winner is: ', first_4_digits, stars, last_3_numbers,
      sep='')
