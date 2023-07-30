number_1 = int(input("Введите первое число массива: "))
number_2 = int(input("Введите последне число массива: "))
delitel = int(input("На какое число делим?: "))
i = int

# >>> list(range(number_1, number_2)) List и range не пойму разницу

for i in range(number_1, number_2):
    if i % delitel == 0:
        print(i)






