#include "../include/rsa.hpp"
#include <stdio.h>

int main()
{
    auto sys = new RSA();
    sys->generate_key(); // sys->generate_key(23, 31);
    sys->print_key();

    int m = 10, e = sys->encrypt(m), d = sys->decrypt(e);
    printf("Original message: %d\n", m);
    printf("Encrypted message: %d\n", e);
    printf("Decrypted message: %d\n", d);
}
