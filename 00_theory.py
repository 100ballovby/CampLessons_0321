'''Переменные - коробочка для сохранения значений
имя_переменной =(присвоить) значение_переменной
'''

number_1 = 12  # int <- целочисленный тип
number_2 = 67.345  # float <- число плавающей точкой

print(type(number_2))  # вывести(тип_данных(number_1))
'''
+, -, *, /
** <- возвести в степень (2 ** 3 = 8)
/ <- деление (10 / 3 = 3.3333)
// <- целочисленное деление (10 // 3 = 3)
% <- вернуть остаток от деления (10 % 3 = 1)

+= <- сложение с присваиванием
-= <- разность с присваиванием
x= <- любое действие сверху с присваиванием
'''
print('Значение переменной number_2', number_2)
number_2 += 17  # number_2 = number_2 + 17
print('Новое значение переменной', number_2)