alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', '?', '!']

inkey = list(input("Введите ключевое слово "))
insms = list(input("Введите Ваше сообщение "))
outkey = []
t = 0

for x in range(0, len(insms)):
    outkey.append(inkey[t])
    t = (t + 1) % len(inkey)

print("Ключ: ", "".join(outkey))
crypted = []

for x in range(0, len(insms)):
    crypted.append(alphabet[(alphabet.index(insms[x]) + alphabet.index(outkey[x])) % len(alphabet)])

print('Зашифрованное: ', "".join(crypted))
decrypted = []

for x in range(0, len(crypted)):
    decrypted.append(alphabet[(alphabet.index(crypted[x]) - alphabet.index(outkey[x])) % len(alphabet)])

print('Дешифрованное: ', "".join(decrypted))
