# Ввод показаний счетчика
prev = int(input("Введите показания "))
curr = int(input("Введите показания "))

# Расчет объема использованного газа
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

# Расчет суммы оплаты
if used <= 300:
    payment = 21.0
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

# Расчет средней цены за кубометр
avg_price = payment / used

# Вывод результатов
print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev} {curr} {used} {payment:.2f} {avg_price:.2f}")
