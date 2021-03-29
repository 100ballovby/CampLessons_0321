for number in range(1, 11):
    if number == 5:
        continue  # пропуск итерации (ничего не делать)
    elif number == 8:
        break  # выйти из цикла
    else:
        print(f'5 * {number} = {5 * number}')
