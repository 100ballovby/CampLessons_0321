grocery = [('milk', 2), ('cookie', 1), ('apple', 5)]

# hash-таблица - это словарь

grocery_new = dict()  # создал hash-таблицу
grocery_new['milk'] = 2.05
grocery_new['cookies'] = 1
grocery_new['apple'] = 4.99

print(grocery_new)

print(grocery_new['milk'])

######
db = [
    {'username': 'gr', 'password': '9cae54f2fb95079c845046e073bd2a856d6c3e9651a288a7d3bab8c9fa83ea4f'},  # 0
    {'username': 'zodiac', 'password': 'try-to-guess'}  # плохой способ хранения паролей - 1
]

print(db[0]['username'])