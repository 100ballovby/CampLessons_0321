'''
def name(param1, param2):
--->action1
--->action2
--->return result

^ создание функции

name(12, 5) - 1
my_result = name(5, 32) - 2
'''
from random import randint

r = [i ** 2 for i in range(1, 5001) if i % 3 == 0 and i % 5 == 0]

print(f'1: {r}')

r_1 = []
for j in range(5):
    r_1.append(randint(1, 15))
print(r_1)


r_array = [31, 88, 17, -37, 97, -55, -15, -69, 5, 34, 62, -91, 43, 57, 8, 33, -3, -64, -3, 33, 67, -86, -3, 66, 97, 64, 75, -67, 3, 64, 70, 66, -14, 5, 28, 13, 82, -9, 6, -22, 24, -45, -79, -72, 31, 38, 8, 38, 51, -86]


def linear_search(array, number):
    for element in range(len(array) + 1):
        if array[element] == number:
            break
    return element


def binary_search(array, number):
    low = 0
    mid = len(array) // 2
    high = len(array) - 1

    while low <= high and array[mid] != number:
        mid = (low + high) // 2
        if number > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return mid


print(linear_search(r_array, 17))
print(linear_search(r_array, -64))
# 1 - 100 = 99 попыток

r_array.sort()  # сортировка
print(r_array)
print(binary_search(r_array, 17))
# 1 - 100 = 7 попыток
# 100 -> 50 -> 25 -> 12 -> 6 -> 3 -> 1
