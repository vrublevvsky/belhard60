from random import randint
a = randint(1, 30)
b = int(input())
y = 5
while not a == b:
    print("не угадал")
    print('осталось попыток')
    y = y - 1
    print(y)
    if a > b:
        print('число больше')
    else:
        print('число меньше')
    b = int(input())
print('верно')