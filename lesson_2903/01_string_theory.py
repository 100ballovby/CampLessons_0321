'''Строки - последовательность символов, заключенная в кавычки'''

name = 'Jagor' # str
print(f'Тип переменной name = {type(name)}')
hobby = 'photo'

print(f'Hello, {name}!')

greeting = "Hello! I'm a Python developer!"
print('Hello! \nI\'m a Python developer!')  # \n <- символ создания новой строки, \ - символ экранирования

print(hobby[0])  # [index] <- порядковый номер буквы в строке
print(greeting[0:6])  # [x:y] <- вывести значения с индекса х до индекса у

'''
+ <- конкатенация ('a' + '5' = 'a5') сложение строк ('a' + 5 = Error)
* <- умножение ('a' * 5 = 'aaaaa') | ('a' * '5' = Error)
'''
