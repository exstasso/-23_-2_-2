#Продолжение финансового планирования
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
moin = 0
money_capital = 0
while moin < months:
    moin += 1
    money_capital += spend - salary
    spend *= (increase + 1)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.2f}")
