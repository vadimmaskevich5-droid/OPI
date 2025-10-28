
import random
import time

# Ввод количества примеров
N = int(input("Введите количество примеров: "))

correct = 0
total_time = 0

print()

# Основной цикл
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    
    print(f"Вопрос {i+1}/{N}")
    
    while True:
        try:
            start = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spent = time.time() - start
            
            if answer == a * b:
                print(f"Верно! (Время: {time_spent:.1f} сек)")
                correct += 1
            else:
                print(f"Неверно! Правильно: {a*b} (Время: {time_spent:.1f} сек)")
            
            total_time += time_spent
            break
        except:
            print("Пожалуйста, введите целое число!")
    
    print()

# Статистика
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time/N:.1f} сек")
print(f"Правильных ответов: {correct}/{N}")
print(f"Процент правильных: {correct/N*100:.1f}%")