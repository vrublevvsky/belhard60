#Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = int(input())
c = 1
some_list = list()
while n > 0:
    some_list.append(2 ** c)
    c += 1
    n -= 1
print(sorted(some_list))
