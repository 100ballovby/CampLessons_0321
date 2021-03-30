def countdown(n):
    print(n)
    if n <= 0:
        print('все')
    else:
        countdown(n - 1)


countdown(3)
print()
countdown(4)
print()
countdown(0)