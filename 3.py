import random

name1 = input("имя 1 ")
name2 = input("ДАЙ РОБОТУ ИМЯ ")
quantitySweets = int(input("Введите количество конфет = ")) # количество конфет на столе
countStep = 0  # переменная хода
sweets1 = 0 # инициализация переменной , конфеты, кот берёт первый игрок
sweets2 = 0 # инициализация переменной , конфеты, кот берёт второй игрок
playerID = 0 # айди игрока - по нему определяем победителя на кратность
whoseMove = random.randint(0, 1)
#print(f"Результат рандома {whoseMove} ")
whoseMove = (whoseMove + 1) % 2



while quantitySweets >= 0:
        whoseMove = (whoseMove + 1) % 2
        if whoseMove == 0:


            print(f"Ход {countStep+1}")
            sweets1 = int(input(f"Введите количество конфет, которые возьмёт первый игрок {name1} "))
            while sweets1 <= 0 or sweets1 > 28: # проверка
                sweets1 = int(input("ПОВТОРИТЕ ВВОД! НУЖНО ВЫБРАТЬ от 1 до 28 конфет! "))# проверка
            while quantitySweets - sweets1 < 0:# проверка
                sweets1 = int(input(
                    f"Вы пытаетесь взять {sweets1}, но на столе осталось {quantitySweets}, возьмите от 1 до {quantitySweets} "))# проверка
            quantitySweets = quantitySweets - sweets1
            print(f"Игрок {name1} взял {sweets1} конфет, осталось {quantitySweets} ")
            if quantitySweets == 0 and whoseMove % 2 == 0:
                print(f'Победителем стал {name1}')
                break
            elif quantitySweets == 0 and whoseMove%2==1:
                print(f'Победителем стал {name2}')
                break
            countStep += 1
            playerID+=1

            whoseMove+=1
        else:

            print(f"Ход {countStep+1}")
            sweets2 = random.randint(1,29)
            while quantitySweets - sweets2 < 0:# проверка
                sweets2 = random.randint(1,quantitySweets)
            quantitySweets = quantitySweets - sweets2
            if quantitySweets == 0 and whoseMove % 2 == 0:
                print(f'Победителем стал {name1}')
                break
            elif quantitySweets == 0 and whoseMove%2==1:
                print(f'Победителем стал {name2}')
                break
            print(f"Игрок {name2} взял {sweets2} конфет, осталось {quantitySweets} ")
            countStep+=1
            playerID+=1

            whoseMove+=1
        whoseMove+=1