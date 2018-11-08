#include "../include/rsa.hpp"
#include "../include/algor.hpp"
#include <stdio.h>
#include <stdlib.h>

RSAKey *RSA::generate_key(unsigned int p, unsigned int q)
{
    RSAKey key;

    if (!p) p = generate_prime(1);
    if (!q) q = generate_prime(p);

    key.p = p;
    key.q = q;
    key.n = key.p * key.q;
    key.phi = (key.p - 1) * (key.q - 1);

    long long int gcd = 0, x, y;

    do {
        key.e = generate_e(key.phi);
        gcd = extended_euclidean_algorithm(key.e, key.phi, x, y);
    } while (gcd != 1 || x < 0);

    key.d = x;

    this->key = key;

    return &this->key;
}

void RSA::print_key()
{
    printf(
        "{p: %d, q: %d, n: %d, phi: %d, e: %d, d: %d}\n",
        this->key.p, this->key.q, this->key.n, this->key.phi, this->key.e, this->key.d
    );
}

int RSA::public_key()
{
    return this->key.d;
}

int RSA::private_key()
{
    return this->key.e;
}

int RSA::encrypt(int m)
{
    return fast_modular_exponentiation_algorithm(m % this->key.n, this->key.d, this->key.n);
}

int RSA::decrypt(int s)
{
    return fast_modular_exponentiation_algorithm(s, this->key.e, this->key.n);
}
