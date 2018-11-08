#include "../include/algor.hpp"
#include <math.h>
#include <vector>
#include <numeric>
#include <time.h>

static int num_bits(unsigned long long int n){
    int c = 0;
    for (; n; c++) n >>= 1;

    return c;
}

static long long int random(unsigned long long int min, unsigned long long int max)
{
   static bool first = true;
   if (first)
   {
      srand( time(NULL) ); //seeding for the first time only!
      first = false;
   }
   return min + rand() % (( max + 1 ) - min);
}

static bool is_prime(long long int n)
{
    if (n < 1) return false;
    else if (n < 3) return true;
    else if (n % 2 == 0 || n % 3 == 0) return false;

    int i = 5;
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }

    return true;
}

unsigned int fast_modular_exponentiation_algorithm(long long int a, long long int z, long long int n)
{
    int bits = num_bits(z);
    long long int mul = 1;
    std::vector<long long int> powers_of_2, mod_of_powers = { (long long int) pow(a, 1) % n };

    for (int pos = 0; pos != bits; pos++) if (z & (1 << pos)) powers_of_2.push_back((long long int) pos);
    for (long long int i = 1, power = 1 << i; power <= z; power = 1 << (++i)) mod_of_powers.push_back(mod_of_powers.back() * mod_of_powers.back() % n);
    for (auto e : powers_of_2) mul *= mod_of_powers.at(e);

    return mul % n;
}

unsigned int extended_euclidean_algorithm(long long int a, long long int b, long long int &x, long long int &y) {
    if (b == 0) { x = 1; y = 0; return a; }

    long long int x1, y1, gcd = extended_euclidean_algorithm(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;

    return gcd;
}

unsigned int generate_e(unsigned long long int phi)
{
    long long int e;
    do e = random(2, phi - 1); while (std::gcd(e, phi) != 1);

    return e;
}

unsigned int generate_prime(unsigned long long int min)
{
    long long int number;

    do number = random(min, 80);
    while (!is_prime(number));

    return number;
}
