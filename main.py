'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) (доп) Подумайте как наделить бота ""интеллектом""'''
import random

name1 = input("имя 1 ")
name2 = input("имя 2 ")
quantitySweets = int(input("Введите количество конфет = ")) # количество конфет на столе
#playersChoice = [1,2]
#whoStart = random.choice(playersChoice)
#print(whoStart)
countStep = 0  # переменная хода
sweets1 = 0 # инициализация переменной , конфеты, кот берёт первый игрок
sweets2 = 0 # инициализация переменной , конфеты, кот берёт второй игрок
playerID = 0 # айди игрока - по нему определяем победителя на кратность


while quantitySweets >= 0:
        print(f"Ход {countStep+1}")
        sweets1 = int(input(f"Введите количество конфет, которые возьмёт первый игрок {name1} "))
        while sweets1 <= 0 or sweets1 > 28: # проверка
            sweets1 = int(input("ПОВТОРИТЕ ВВОД! НУЖНО ВЫБРАТЬ от 1 до 28 конфет! "))# проверка
        while quantitySweets - sweets1 < 0:# проверка
            sweets1 = int(input(
                f"Вы пытаетесь взять {sweets1}, но на столе осталось {quantitySweets}, возьмите от 1 до {quantitySweets} "))# проверка
        quantitySweets = quantitySweets - sweets1
        print(f" Игрок {name1} взял {sweets1} конфет, осталось {quantitySweets} ")
        if quantitySweets == 0 and playerID % 2 == 0:
            print(f'Победителем стал {name1}')
            break
        elif quantitySweets == 0 and playerID%2==1:
            print(f'Победителем стал {name2}')
            break
        countStep += 1
        playerID+=1
        print(playerID)

        print(f"Ход {countStep+1}")
        sweets2 = int(input(f"Введите количество конфет, которые возьмёт первый игрок {name2} "))
        while sweets2 <= 0 or sweets2 > 28:# проверка
            sweets2 = int(input("ПОВТОРИТЕ ВВОД! НУЖНО ВЫБРАТЬ от 1 до 28 конфет! "))# проверка
        while quantitySweets - sweets2 < 0:# проверка
            sweets2 = int(input(
                f"Вы пытаетесь взять {sweets2}, но на столе осталось {quantitySweets}, возьмите от 1 до {quantitySweets} "))# проверка
        quantitySweets = quantitySweets - sweets2
        if quantitySweets == 0 and playerID % 2 == 0:
            print(f'Победителем стал {name1}')
            break
        elif quantitySweets == 0 and playerID%2==1:
            print(f'Победителем стал {name2}')
            break
        print(f" Игрок {name2} взял {sweets2} конфет, осталось {quantitySweets} ")
        countStep+=1
        playerID+=1
        print(playerID)

'''
def CheckMethod():
  global xod, quantitySweets
  while quantitySweets > 0:
      xod = int(input("Введите количество конфет, которое вы хотите взять "))
      while xod <= 0 or xod > 28:
          xod = int(input("ПОВТОРИТЕ ВВОД! НУЖНО ВЫБРАТЬ от 1 до 28 конфет! "))
      while quantitySweets - xod < 0:
          xod = int(input(
              f"Вы пытаетесь взять {xod}, но на столе осталось {quantitySweets}, возьмите от 1 до {quantitySweets} "))

      quantitySweets = quantitySweets - xod
      print(f"Осталось {quantitySweets} конфет ")'''

'''
CheckMethod()'''
