per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # вводим условия процентовки
money = input("Введите сумму вклада:") # переменная, для ввода суммы вклада
deposit = [int(int(money) * per_cent.get("ТКБ") / 100),
           int(int(money) * per_cent.get("СКБ") / 100),
           int(int(money) * per_cent.get("ВТБ") / 100),
           int(int(money) * per_cent.get("СБЕР") / 100),] # работа с каждым отдельным банком, вычисление процента от суммы money
print(str("Депосит в банках ТКБ, СКБ, ВТБ, СБЕР"), deposit) # выводим получвшиеся значения
max_deposit = max(deposit) # определяем максимальное значение из списка
print(str("Максимальная сумма, которую вы можете заработать"), max_deposit) # выводим максимальное значение из списка
123
