# Ввод последовательности пакетов
packets = input("Введите последовательность пакетов (0 и 1): ")

# Проверка длины строки
if len(packets) < 5:
    print("Ошибка: длина строки должна быть не меньше 5")
    exit()

# Проверка корректности символов
for char in packets:
    if char not in '01':
        print("Ошибка: используйте только символы '0' и '1'")
        exit()

# Общее количество пакетов
total_packets = len(packets)
print(f"• Общее количество пакетов: {total_packets}")

# Количество потерянных пакетов (нулей)
lost_packets = packets.count('0')
print(f"• Количество потерянных пакетов: {lost_packets}")

# Поиск самой длинной последовательности нулей
max_lost_streak = 0
current_streak = 0

for packet in packets:
    if packet == '0':
        current_streak += 1
        if current_streak > max_lost_streak:
            max_lost_streak = current_streak
    else:
        current_streak = 0

print(f"• Длина самой длинной последовательности потерянных пакетов: {max_lost_streak}")

# Процент потерь
loss_percentage = (lost_packets / total_packets) * 100
print(f"• Процент потерь: {loss_percentage:.1f}%")

# Оценка качества связи
if loss_percentage <= 1:
    quality = "отличное качество"
elif loss_percentage <= 5:
    quality = "хорошее качество"
elif loss_percentage <= 10:
    quality = "удовлетворительное качество"
elif loss_percentage <= 20:
    quality = "плохое качество"
else:
    quality = "критическое состояние сети"

print(f"• Качество связи: {quality}")
