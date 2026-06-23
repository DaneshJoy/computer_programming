grades = {'Math': 11.7,
          'Physics': 15,
          'Programming': 18.5}


for k, v in grades.items():
    print(k, '-->>', v)


print('-*-' * 10)


s = 0
for grade in grades.values():
    s = s + grade

average = s / len(grades)

print('Average:', round(average, 2))



