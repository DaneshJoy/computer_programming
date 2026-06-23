import time

start = time.time()
for i in range(1, 51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    time.sleep(0.2)
end = time.time()

print('Total time:', end-start, 'seconds')