import random

def num_bits(n: int) -> int:
    c = 0
    while (n):
        n >>= 1
        c += 1
    return c

def generate_e(phi: int) -> int:
    e = random.randint(2, phi - 1)
    while (std::gcd(e, phi) != 1):
        e = random.randint(2, phi - 1)
    return e

def generate_prime(min: int) -> int:
    number = random.randint(min, 80)
    while not is_prime(number):
        number = random.randint(min, 80)
    return number

def is_prime(n: int) -> int:
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True
