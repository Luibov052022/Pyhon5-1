# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('4-1.txt', 'r') as data:
    input_string = data.readline()
print('Исходный текст') 
print(input_string)    
symbols = [let for let in input_string]
letters=[]
counts = []
count = 1

for i in range (1, len(symbols)):
    if symbols[i-1] == symbols[i]:
        count+=1
        
    else:
        letters.append(symbols[i-1])
        counts.append(count)
        count=1
letters.append(symbols[len(symbols)-1]) 
counts.append(count) 
print('Зашифрованный текст')    
zipped = zip(letters, counts)
print(*zipped)
string = map(lambda x,y: x*y, letters, counts)
with open('4-2.txt', 'w') as data:
    data.write('New text' + '\n' + ''.join(string))

