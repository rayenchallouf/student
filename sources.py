from math import sqrt
import random
import string


def generate_password():
    length = 9
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    password = [random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(symbols)]
    rest = length - len(password)
    all_characters = lowercase + uppercase + digits + symbols
    for i in range(rest):
        password.append(random.choice(all_characters))
    random.shuffle(password)
# Convertissez la liste de caractères en une chaîne de caractères
    password = ''.join(password)
    return password


def contains_symbol(s):
    for char in s:
        if not char.isalnum():
            return True
    return False


def contains_number(s):
    for char in s:
        if char.isnumeric():
            return True
    return False


def contains_uppercase(s):
    for char in s:
        if char.isupper():
            return True
    return False


def contains_lowercase(s):
    for char in s:
        if char.islower():
            return True
    return False


def pgcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def ppcm(a, b):
    p = a
    while p % b != 0:
        p += a
    return p


def premier(a):
    i = 1
    while(a % i == 0) or (i > sqrt(a)):
        i += 1
    return i > sqrt(a)


def fact(n):
    f = 1
    for i in range(1, n):
        f *= i
    return f

# n number and b for bass(2-16)


def b10_to_2_16(n, b):
    ch = ""
    while(n == 0):
        r = n % b
        if r < 10:
            c = chr(r + 48)
        else:
            c = chr(r + 55)
        ch += c
        n = n // b
    return ch
# ch for chain b for bass


def b2_16_to_b10(ch, b):
    n = 0
    p = 1
    for i in range(len(ch) - 1, 0, -1):
        if "0" <= ch[i] < "9":
            k = int(ch[i])
        else:
            k = ord(ch[i]) - 55
        n = n + p * k
        p = p * b
    return n


def triangleP(M, n):
    M[0, 0] = 1
    for i in range(1, n + 1):
        M[i, 0], M[i, i] = 1, 1
        for j in range(1, i):
            M[i, j] = M[i - 1, j] + M[i - 1, j - 1]
