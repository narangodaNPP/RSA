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
    # generate p,q prime numbers
    p, q = generate_prime_number(1000, 5000), generate_prime_number(1000, 5000)

    # select different values for p,q
    while p == q:
         q = generate_prime_number(1000, 5000)

    n = p * q
    totient_n = (p - 1) * (q - 1)

    e = random.randint(3, totient_n-1)

    # generate e that coprime with totient_n
    while gcd(e, totient_n) != 1:
        e = random.randint(3, totient_n-1)

    d = multiplicative_inverse(e, totient_n)

    message = "Narangoda N.P.P"

    encoded_message = [ord(c) for c in message]  # message encode into ascii

    cipher_text = [pow(m, e, n) for m in encoded_message]  # turned into cipher text => (m^e)%n

    decoded_message = [pow(c, d, n) for c in cipher_text]  # cipher text decoded into ascii => (c^d)%n

    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"d = {d}")
    print(f"Message : {message}")
    print(f"Encoded Message = {encoded_message}")
    print(f"Ciphertext = {cipher_text}")
    print(f"Decrypted Message = {decoded_message}")

    # print the string value back
    print(f"Decoded Message: {''.join(chr(ch) for ch in decoded_message)}")

