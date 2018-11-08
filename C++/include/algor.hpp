/**
 * |----------------------------------------------------------------|
 * | Algorithms to implement the RSA cryptosystem Operations module |
 * |----------------------------------------------------------------|
 *
 * Copyright 2018 Erik Campobadal <soc@erik.cat>
 * https://erik.cat
 */

#ifndef modular_hpp
#define modular_hpp

unsigned int fast_modular_exponentiation_algorithm(long long int a, long long int z, long long int n);
unsigned int extended_euclidean_algorithm(long long int a, long long int b, long long int &x, long long int &y);
unsigned int generate_e(unsigned long long int phi);
unsigned int generate_prime(unsigned long long int min);

#endif
