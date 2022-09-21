#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

num1 = input()
num2 = input()
num3 = input()
positive = 0
negative = 0
if int(num1) > 0:
    positive += 1
else:
    negative += 1
if int(num2) > 0:
    positive += 1
else:
    negative += 1
if int(num3) > 0:
    positive += 1
else:
    negative += 1
print(f"Положительных {positive}, отрицательных {negative} ")
