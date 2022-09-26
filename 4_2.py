#Без использования collections, написать программу, которая будет
#создавать словарь для подсчитывания количества вхождений каждой
#буквы в текст введенный с клавиатуры

some_txt = input()
some_list = []
some_txt = some_txt.lower()
some_txt = some_txt.replace(" ", "")
lng_stroke = len(some_txt)
some_list.extend(some_txt)
some_list.sort()
some_dict = dict.fromkeys(some_list, 1)
print(some_list)
print(some_dict)
print(lng_stroke)