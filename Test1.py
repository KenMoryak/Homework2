name = input("Введите свое имя: ")
age_string = input("Введите возраст: ")
if age_string.isdigit():
    age=int(age_string)
    print("Возраст введен верно")
elif age_string == 'zz':
    print("22 ==22")

else:
    print("Возраст введен неверно")

print(age_string.isdigit())
print(f"Ваще имя: {name} {age_string}")
