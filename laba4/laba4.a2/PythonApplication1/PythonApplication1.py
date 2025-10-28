# Прямоугольник
n = int(input("Введите n: "))
m = int(input("Введите m: "))

print("ПРЯМОУГОЛЬНИК:")
for i in range(n):
    for j in range(m):
        print('#', end='')
    print()

print()

# Правый треугольник
print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(n):
    for j in range(i + 1):
        print('#', end='')
    print()

print()

# Рамка
print("РАМКА:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
