extern crate rand;
use self::rand::{thread_rng, Rng};

pub fn is_prime(n: u128) -> bool
{
    if n <= 1 { return false; }
    else if n <= 3 { return true; }
    else if n % 2 == 0 || n % 3 == 0 { return false; }

    let mut i: u128 = 5;
    while i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 { return false; }
        i += 6;
    }

    return true;
}

pub fn num_bits(mut n: u128) -> u8 {
    let mut c: u8 = 0;
    while n != 0 {
        n >>= 1;
        c += 1;
    }

    return c;
}

pub fn random_num(a: u32, b: u32) -> u128
{
    return rand::thread_rng().gen_range(a, b) as u128;
}

pub fn fast_modular_exponentiation_algorithm(a: u128, z: u128, n: u128) -> u128
{
    let bits: u128 = num_bits(z) as u128;
    let mut mul: u128 = 1;
    let mut powers_of_2: Vec<usize> = vec![];
    let mut mod_of_powers: Vec<u128> = vec![a.pow(1) % n];

    //for (int pos = 0; pos != bits; pos++) if (z & (1 << pos)) powers_of_2.push_back((long long int) pos);
    let mut pos: u128 = 0;
    while pos != bits {
        if z & (1 << pos) != 0 {
            powers_of_2.push(pos as usize);
        }
        pos += 1;
    }

    //for (long long int i = 1, power = 1 << i; power <= z; power = 1 << (++i)) mod_of_powers.push_back(mod_of_powers.back() * mod_of_powers.back() % n);
    let mut i: u128 = 1;
    let mut power: u128 = 1 << i;
    while power <= z {
        let v: u128 = mod_of_powers[mod_of_powers.len()];
        mod_of_powers.push(v * v % n);
        i += 1;
        power = 1 << i;
    }

    //for (auto e : powers_of_2) mul *= mod_of_powers.at(e);
    for &e in powers_of_2.iter() { mul *= mod_of_powers[e]; }

    return mul % n;
}

pub fn extended_euclidean_algorithm(a: u128, b: u128, x: &mut u128, y: &mut u128) -> u128
{
    if b == 0 { *x = 1; *y = 0; return a; }

    let x1: &mut u128 = &mut 0;
    let y1: &mut u128 = &mut 0;
    let gcd: u128 = extended_euclidean_algorithm(b, a % b, x1, y1);
    //long long int x1, y1, gcd = extended_euclidean_algorithm(b, a % b, x1, y1);

    *x = *y1;
    *y = *x1 - (a / b) * (*y1);

    return gcd;
}
