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
        raise ValueError("Both numbers must be prime.")
    elif numbers[0] == numbers[1]:
        raise ValueError("Numbers cannot be equal.")
    return numbers[0], numbers[1]


def get_phi(p, q):
    return (p - 1) * (q - 1)


def get_e(n, phi):
    e = random.randrange(3, phi)
    g = gcd(e, phi) + gcd(e, n)
    while g != 2:
        e = random.randrange(3, phi)
        g = gcd(e, phi) + gcd(e, n)
    return e


def get_d(e, phi):
    return pow(e, -1, phi)


def encrypt(text, key):
    e, n = key
    cipher = ''.join(chr(pow(ord(char), e, n)) for char in text)
    return cipher


def decrypt(cipher, key):
    d, n = key
    plaintext = [chr(pow(ord(char), d, n)) for char in cipher]
    return ''.join(plaintext)


need = input("Do you want to encrypt or decrypt? Enter 'en' or 'de': ")

match need:
    case 'en':
        prime_numbers = get_prime_numbers([int(x) for x in input("Enter any two prime numbers: ").split()])
        n = prime_numbers[0] * prime_numbers[1]
        phi = get_phi(prime_numbers[0], prime_numbers[1])
        e = get_e(n, phi)
        d = get_d(e, phi)
        public = e, n
        private = d, n
        print(f"{public} | {private}")
        message = input("Enter a message: ")
        encrypted = encrypt(message, public)
        print(f"Your encrypted message is: {encrypted}")
        decrypted = decrypt(encrypted, private)
        if decrypted == message:
            print("Success!")
        else:
            print("Failure. Let's try again!")
    case 'de':
        private = tuple(int(x) for x in input("Enter a private key: ").split())
        decrypted = decrypt(input("Enter a cipher: "), private)
        print(f"Your decrypted message is: {decrypted}")
    case _:
        raise ValueError(f"{need} is neither 'en' nor 'de'.")
