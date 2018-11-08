/**
 * |-------------------------|
 * | RSA cryptosystem module |
 * |-------------------------|
 *
 * Copyright 2018 Erik Campobadal <soc@erik.cat>
 * https://erik.cat
 */

#ifndef rsa_hpp
#define rsa_hpp

typedef struct {
    unsigned long long int p, q, phi, n, e, d;
} RSAKey;

class RSA
{
    RSAKey key;

    public:
        RSAKey *generate_key(unsigned int p = 0, unsigned int q = 0);
        void print_key();
        int public_key();
        int private_key();
        int encrypt(int m);
        int decrypt(int s);
};

#endif
