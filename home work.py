# Задача 2: Найдите сумму цифр трехзначного числа.
a = int(input("Введите любое трехзначное число: "))
a1 = a // 100 
a2 =(a%100) // 10 
a3 = a % 10
if 100<=a<=999:
    print(f'Сумма чисел введенного числа равна: {a1+a2+a3}')
else:
    print('Число не трехзначное')
    
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
""" Все вместе они сделали x+x+(x+x)*2=6x журавликов. Отсюда уравнение: 6x=S """

s = int(input ("Сколько журавликов сделал каждый ребенок: "))
print (f'Общее количество журавликов: {s}', f'Петя сделал {s//6} журавликов', 
       f'Катя сделала {(s//6)*4} журавликов', f'Сережа сделал {s//6} журавликов') 

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
# счастливость билета.

a = int(input("Введите номер билета: "))
a1 = a//100000
a2 = (a%100000)//10000
a3 = (a%10000)//1000
a4 = (a%1000)//100
a5 = (a%100)//10
a6 = a%10
if 100000<=a<=999999 and a1+a2+a3 == a4+a5+a6:
    print('Билет счастливый')
else:
    print('Билет не счастливый или вы ввели неверный номер')
    
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите число долек по горизонтали: '))
m = int(input('Введите число долек по вертикали: '))
k = int(input('Введите число долек которое хотите отломить: '))
if k < m * n and (k % m == 0 or k % n == 0):
    print('шоколадку можно разломить на два прямоугольника')
else:
    print('шоколадку нельзя разломить на два прямоугольника')
