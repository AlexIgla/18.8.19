x = 0
tickets = int(input("Введите количество билетов:"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        x += 0
    elif 18 <= age <= 25:
        x += 990
    elif age > 25:
        x += 1390
if tickets > 3:
    x -= x / 100 * 10
print("Стоимость Ваших билетов", x)