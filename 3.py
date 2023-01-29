'''Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
385916 -> yes
123456 -> no'''

a = input('Введите номер билета: ')

b = int((a[0]) + (a[1]) + (a[2]))
c = int((a[-1]) + (a[-2]) + (a[-3]))    #по аналогии 1 задачи, извлекала 3 первых символа и 3 последних

if b := c:
    print('yes')
else:
    print('no')

