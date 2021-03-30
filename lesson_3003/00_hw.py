from random import randint  # выдать псевдослучайное число в промежутке от a до b

secret_number = randint(1, 101)
attempts = 1

print('Я загадал число от 1 до 100, угадай его!')
guess = int(input('Введи число: '))

while guess != secret_number or attempts <= 7:

    if guess > secret_number:
        print('Мое число меньше!')
    elif guess < secret_number:
        print('Мое число больше!')
    elif guess == secret_number:
        break
    attempts += 1
    guess = int(input('Введи число: '))

if guess != secret_number:
    print(f'Ты не угадал! Я загадал число: {secret_number}')
else:
    print(f'Ты угадал за {attempts} попыток')
