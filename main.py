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
quantitySweets = int(input("Введите количество конфет = "))
playersChoice = [1,2]
whoStart = random.choice(playersChoice)

countStep = 0
sweets1 = 0
sweets2 = 0
if whoStart == 1:
    player1 = name1
    print(f" Начинает ходить первый игрок {name1}")
else:
    player2 = name2
    print(f" Начинает ходить второй игрок {name2}")



while quantitySweets > 0:
    if whoStart==1:
        print(f"Ход {countStep+1}")
        sweets1 = int(input(f"Введите количество конфет, которые возьмёт первый игрок {name1} "))
        quantitySweets = quantitySweets - sweets1
        print(f" Игрок {player1} взял {sweets1} конфет, осталось {quantitySweets} ")
        countStep+=1
    elif whoStart==2:
        print(f"Ход {countStep+1}")
        sweets2 = int(input(f"Введите количество конфет, которые возьмёт первый игрок {name2} "))
        quantitySweets = quantitySweets - sweets2
        print(f" Игрок {player2} взял {sweets2} конфет, осталось {quantitySweets} ")
        countStep+=1
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
