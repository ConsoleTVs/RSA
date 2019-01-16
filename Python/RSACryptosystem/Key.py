from random import randint
from fractions import gcd
from sympy import isprime, randprime

class Key:

    # The p and q used by the key
    p, q = 0, 0
    # n = p * q
    n = 0
    # phi = (p - 1) * (q - 1)
    phi = 0
    # The e and d used by the key. d == e**-1 mod phi
    e, d = 0, 0

    def __init__(self, p = None, q = None):
        # Determine if p and q are defined.
        if not p: p = randprime(50, 200)
        while not q or p == q: q = randprime(50, 200)
        # Check if p and q are primes
        if not isprime(p) or not isprime(q):
            raise Exception("The provided p and q are invalid.")
        # Basic assignments.
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        # Calculate e and d.
        self.__generate_e_and_d()

    def __generate_e_and_d(self):
        gcd = 0
        self.e = self.__generate_e(self.phi)
        gcd, x, y = self.__extended_euclidean_algorithm(self.e, self.phi)
        while gcd != 1 or x < 0:
            self.e = self.__generate_e(self.phi)
            gcd, x, y = self.__extended_euclidean_algorithm(self.e, self.phi)
        self.d = x

    def __generate_e(self, phi):
        e = randint(2, phi - 1)
        while gcd(e, phi) != 1: e = randint(2, phi - 1)
        return e

    def __extended_euclidean_algorithm(self, a, b):
        # Initial x setup. x1 is the last calculated x,
        # and it's initialized to 1
        x1, x = 1, 0
        # Initial y setup (The same as x)
        y1, y = 1, 0
        # While b is diferent from 0
        while b:
            # Calculate the current quotient out of a / b.
            quotient = a // b
            # Set the view value of x and update the last x.
            x, x1 = x1 - quotient * x, x
            # The same for y.
            y, y1 = y1 - quotient * y, y
            # Update a and v values.
            a, b = b, a % b
        # Return the tyiple value g, x, y
        return a, x1, y1

    def length(self):
        return len(format(self.n, 'b'))

    def public(self):
        return {
            'n': self.n,
            'e': self.e
        }

    def private(self):
        return {
            'p': self.p,
            'q': self.q,
            'phi': self.phi,
            'd': self.d
        }

    def print(self):
        print({
            'length': self.length(),
            'public': self.public(),
            'private': self.private()
        })
