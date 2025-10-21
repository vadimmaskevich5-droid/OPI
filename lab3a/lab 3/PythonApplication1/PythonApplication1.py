
x1 = int(input("Введите число x"))
y1 = int(input("Введите число y"))
x2 = int(input("Введите число x"))
y2 = int(input("Введите число y"))


if (x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0):
    print("Yes, I")
elif (x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0):
    print("Yes, II")
elif (x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0):
    print("Yes, III")
elif (x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0):
    print("Yes, IV")
else:
    print("No")
