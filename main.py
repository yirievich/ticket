tickets = int(input("Введите необходимое количество билетов:\n"))
num = []
count = 1
while count != tickets+1 :
    print(f"Введите возраст посетителя №{count}:")
    age = int(input())
    if age < 18 :
        price = 0
    elif 18 <= age < 25 :
        price = 990
    else :
        price = 1390
    num.append(price)
    count += 1
if len(num)>3:
    print("Общая стоимость ваших билетов с учетом 10% скидки:", int(sum(num) * 0.9))
else:
    print("Общая стоимость ваших билетов:", sum(num))
