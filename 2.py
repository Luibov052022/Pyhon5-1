#Создайте программу для игры с конфетами человек против человека.

import random as rnd
 
candy = 2021
vin = 0
while candy > 0:
    player=int(input('Сколько конфет берете? '))
    if (player > 28 or player > candy) and player > 0:
        print('неверный ввод')
        break
    else:
        candy-=player
        print(f'осталось конфет {candy}')  
        vin=1
    if candy == 0:
        break  
    if  candy > 28:             
        bot = rnd.randint(1, 28)
        vin=2
    else:
        bot = rnd.randint(1, candy)
        vin=2
    print(f'бот взял {bot} конфет')
    candy-= bot
    print(f'осталось конфет {candy}') 
    
    
if vin==1:
    print('победил игрок!')
else:
    print('победил бот!')    