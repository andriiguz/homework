from random import randint


def prime(mn, mx):
    global x
    k = 0
    exitflag = False
    while temp == 0:
        x = randint(mn, mx)
        for j in range(2, x):
            if x % j == 0:
                k += 1
        if k == 0:
            exitflag = True
        else:
            k = 0
        if exitflag:
            break
    return x


def testprime(x):
    global primestatus
    primestatus = False
    k = 0
    exitFlag = False
    for j in range(2, x):
        if x % j == 0:
            k += 1
    if k == 0:
        exitFlag = True
    else:
        k = 0
    if exitFlag:
        primestatus = True
    return primestatus


def gcd(a, b):
    global c
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    c = a
    return c


temp = 0
x = 0

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', '?', '!']

numbersal = []

while len(numbersal) < 57:
    x = randint(11, 71)
    if x not in numbersal:
        numbersal.append(x)

prime(71, 307)
p = x
print("p =", p)

prime(71, 307)
q = x
print("q =", q)

mod = p * q
print("mod =", mod)

fi = (p - 1) * (q - 1)
print("fi =", fi)

e = 0
x = 2
while x < fi:
    if testprime(x) and gcd(fi, x) == 1:
        e = x
        break
    else:
        x += 1

print("e =", e)
d = 3

x = 2
while temp == 0:
    if (x * e) % fi == 1:
        d = x
        break
    x += 1

print("d =", d)

insms = list(input("Введите сообщение "))
coverted = []
crypt = []
decrypt = []

for x in range(0, len(insms)):
    coverted.append(numbersal[(alphabet.index(insms[x]))])
print("Преобразованное в значения:", coverted)

for x in range(0, len(insms)):
    crypt.append(coverted[x] ** e % mod)

print("Зашифрованное: ", crypt)

for x in range(0, len(insms)):
    decrypt.append(crypt[x] ** d % mod)

print("Дешифрованное в значения: ", decrypt)

decryptsymbols = []
for x in range(0, len(insms)):
    decryptsymbols.append(alphabet[numbersal.index(decrypt[x])])

print('Дешифрованное: ', "".join(decryptsymbols))
