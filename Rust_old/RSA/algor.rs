use std::rand::{OsRng, Rng};

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

pub fn random(a: u128, b: u128)
{

}
