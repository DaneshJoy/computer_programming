grades = []
while True:
    grade = input('Enter the grade (or "x" to finish): ')
    if grade.lower() == 'x':
        break
    try:
        grade = float(grade)
        grades.append(grade)
    except:
        print('Entered grade is not valid!')


# Method 1 (without loop)
average1 = sum(grades) / len(grades)

# Method 2 (using for loop)
n = 0
s = 0
for grade in grades:
    n = n + 1      # holds the number of items
    s = s + grade  # holds the sum of items

average2 = s / n

print('Average 1:', round(average1, 4))
print('Average 2:', round(average2, 4))