import string

# Ввод пароля
password = input("Введите пароль ")

# Список для хранения ошибок
errors = []

# Проверка длины пароля
if len(password) != 8:
    errors.append("Длина пароля не равна 8")

# Проверка наличия заглавных букв
if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")

# Проверка наличия строчных букв
if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")

# Проверка наличия цифр
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

# Проверка наличия специальных символов
special_chars = ['*', '-', '#']
if not any(symbol in special_chars for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

# Проверка на недопустимые символы
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

# Вывод результата
if len(errors) == 0:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)
