money = int(input("Сумма вклада: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

for value in per_cent.values():
   result = int(money / 100 * value)
   deposit.append(result)
print("Максимальная сумма, которую вы можете заработать - ",max(deposit))