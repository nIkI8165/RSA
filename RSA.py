import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_prime_numbers(numbers):
    if not (is_prime(numbers[0]) and is_prime(numbers[1])):
        raise ValueError("both numbers must be prime")
    elif numbers[0] == numbers[1]:
        raise ValueError("numbers cannot be equal")
    return numbers[0], numbers[1]


def get_phi(p, q):
    return (p - 1) * (q - 1)


def get_e(n, phi):
    e = random.randrange(3, phi)
    g = gcd(e, phi) + gcd(e, n)
    count = 0
    while (g != 2 or get_d(e, phi) == e) and count < 100:
        e = random.randrange(3, phi)
        g = gcd(e, phi) + gcd(e, n)
        count += 1
    if count >= 100:
        raise ValueError("product of two numbers must be greater")
    return e


def get_d(e, phi):
    return pow(e, -1, phi)


def to_ascii(series):
    converted = ''.join(chr(int(n)) for n in series.split())
    return converted


def to_numbers(string):
    converted = ' '.join(str(ord(char)) for char in string)
    return converted


def encrypt(text, key):
    e, n = key
    cipher = ' '.join(str(pow(ord(char), e, n)) for char in text)
    return cipher


def decrypt(cipher, key):
    d, n = key
    plaintext = ''.join(chr(pow(int(x), d, n)) for x in cipher.split())
    return plaintext


need = input("Do you want to generate a pair of keys, encrypt or decrypt? Enter 'ge', 'en' or 'de': ")

match need:
    case 'ge':
        g_in = input("Enter any two prime numbers: ").replace(",", "").replace(";", "")
        prime_numbers = get_prime_numbers([int(x) for x in g_in.split()])
        n = prime_numbers[0] * prime_numbers[1]
        phi = get_phi(prime_numbers[0], prime_numbers[1])
        e = get_e(n, phi)
        d = get_d(e, phi)
        public = e, n
        private = d, n
        print(f"{public} | {private}")
    case 'en':
        u_in = input("Enter a public key: ").replace("(", "").replace(",", "").replace(";", "").replace(")", "")
        public = tuple(int(x) for x in u_in.split())
        encrypted = encrypt(input("Enter a message: "), public)
        t_out = input("Do you want a string of characters or a series of numbers? Enter 'ch' or 'n': ")
        match t_out:
            case 'ch':
                encrypted = to_ascii(encrypted)
            case 'n':
                pass
            case _:
                raise ValueError(f"{t_out} is neither 'ch' nor 'n'")
        print(f"Your encrypted message is: {encrypted}")
    case 'de':
        r_in = input("Enter a private key: ").replace("(", "").replace(",", "").replace(";", "").replace(")", "")
        private = tuple(int(x) for x in r_in.split())
        cipher = input("Enter a cipher: ")
        t_in = input("Is it a string of characters or a series of numbers? Enter 'ch' or 'n': ")
        match t_in:
            case 'ch':
                cipher = to_numbers(cipher)
            case 'n':
                pass
            case _:
                raise ValueError(f"{t_in} is neither 'ch' nor 'n'")
        decrypted = decrypt(cipher, private)
        print(f"Your decrypted message is: {decrypted}")
    case _:
        raise ValueError(f"{need} is neither 'en' nor 'de'")
