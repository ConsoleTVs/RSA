from functools import reduce
from RSA.Key import Key

class RSA:

    # Store the RSA key currently in use.
    key = None

    def __fast_modular_exponentiation(self, a, z, n):
        # Transform the exponent into binary (powers of 2).
        binary = format(z, 'b')
        # Reverse the binary value of the exponent.
        binary_rev = binary[::-1]
        # Save the powers of 2 needed to later use
        powers_of_two = []
        # Add the power of 2^i.
        for i,e in enumerate(binary_rev):
            # Only add if the digit is 1. (1 << i == 2**i)
            if e == '1': powers_of_two.append(1 << i)
        # Calculate mod C of the powers of two.
        mod_of_powers, current_exp = [], 1
        while current_exp <= powers_of_two[-1]:
            if current_exp in powers_of_two:
                mod_of_powers.append(a**current_exp % n)
            current_exp *= 2
        # We multiply the items in the list to get the result and do result mod n.
        return reduce(lambda x, y: x * y, mod_of_powers) % n

    def generate_key(self, p, q):
        self.key = Key(p, q)
        return self.key

    def encrypt(self, plain_text):
        if isinstance(plain_text, str):
            result = []
            for letter in plain_text:
                result.append(self.encrypt(ord(letter)))
        else:
            result = self.__fast_modular_exponentiation(
                plain_text % self.key.n, self.key.e, self.key.n
            )
        return result

    def decrypt(self, cipher_text):
        if isinstance(cipher_text, list):
            result = ""
            for element in cipher_text:
                result += chr(self.decrypt(element))
        else:
            result = self.__fast_modular_exponentiation(
                cipher_text, self.key.d, self.key.n
            )
        return result
