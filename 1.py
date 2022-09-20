# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('1.txt', 'r') as data:
    text = data.readline()
my_list = [element for element in text.split() if (not 'abc' in element)]
with open('1_2.txt', 'w') as data:
    data.write('New text' + '\n' + ' '.join(my_list))
print(*my_list)