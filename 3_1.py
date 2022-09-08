#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

sentence=input()
print(sentence.replace(' ', '-'))
sentence=sentence.split(' ')
sentence={'-'.join(sentence)}
print(sentence)
