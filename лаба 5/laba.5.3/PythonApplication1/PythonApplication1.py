def make_abr(text):
    words = text.split()                # разбиваем на слова
    abr = ""

    for word in words:
        if len(word) >= 3:              # берём только слова длиной 3 и больше
            abr += word[0].upper()

    return abr

s = input()
print(make_abr(s))
