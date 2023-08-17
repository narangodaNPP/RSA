import random
from math import gcd


def is_prime(number):
    """Check the number is prime or not"""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_prime_number(min_value, max_value):
    """Generate random prime number"""
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def multiplicative_inverse(e, totient_n):
    """Get the multiplicative inverse of e"""
    for d in range(3, totient_n):
        if (d * e) % totient_n == 1:
            return d


if __name__ == '__main__':
    p, q = generate_prime_number(1000, 5000), generate_prime_number(1000, 5000)

    while p == q:
         q = generate_prime_number(1000, 5000)

    n = p * q
    totient_n = (p - 1) * (q - 1)

    e = random.randint(3, totient_n-1)
    while gcd(e, totient_n) != 1:
        e = random.randint(3, totient_n-1)

    d = multiplicative_inverse(e, totient_n)

    message = "Pasan Narangoda"

    encoded_message = [ord(c) for c in message]

    cipher_text = [pow(m, e, n) for m in encoded_message]

    plain_text = [pow(c, d, n) for c in cipher_text]

    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"d = {d}")
    print(encoded_message)
    print(cipher_text)
    print(plain_text)

    print(f"Decrypted Message: {''.join(chr(ch) for ch in plain_text)}")

