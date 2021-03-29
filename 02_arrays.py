'''Списки - последовательность элементов, заключенная в квадратные скобки,
имеющая индексы и каждый элемент разделен запятой
'''

cars = ['audi', 'mercedes', 'bmw']  # list
print(f'Тип переменной cars = {type(cars)}')
print(cars)

print(cars[1])  # [index] <- порядковый номер элемента в списке

'''
+ <- ([1, 2, 3] + ['1', '2'] = [1, 2, 3, '1', '2']) сложение списков между собой ([1, 2, 3] + 5 = Error)
* <- умножение ([1, 2, 3] * 5 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) | ([1, 2, 3] * '5' = Error)
'''

cars.append('toyota')  # метод добавления в список
print(cars)
cars.insert(2, 'Alfa Romeo')  # метод вставки на определенную позицию в списке
print(cars)
cars.pop(1)  # метод удаления из списка (индекс указывать не обязательно, но тогда удалится последний элемент)
print(cars)
cars[2] = 'Ferrari'  # замена элемента в списке
print(cars)
