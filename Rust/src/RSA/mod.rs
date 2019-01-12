pub mod algor;

pub struct RSAKey
{
    pub p: u128, pub q: u128, pub phi: u128,
    pub n: u128, pub e: u128, pub d: u128
}

impl RSAKey
{
    pub fn create() -> RSAKey {
        RSAKey { p: 0, q: 0, phi: 0, n: 0, e: 0, d: 0 }
    }
}

pub struct RSASystem
{
    pub key: RSAKey
}

impl RSASystem
{
    pub fn create() -> RSASystem {
        RSASystem { key: RSAKey::create() }
    }

    pub fn generate_key(p: u128, q: u128) -> RSAKey {
        let mut key: RSAKey::create();
        key.p = p;
        key.q = q;

        key.n = key.p * key.q;
        key.phi = (key.p - 1) * (key.q - 1);

        let mut gcd: u128 = 0;
        let mut x: u128;
        let mut y: u128;

        key.e = algor::generate_e(key.phi);
        gcd = algor::extended_euclidean_algorithm(key.e, key.phi, x, y);

        while gcd != 1 || x < 0 {
            key.e = generate_e(key.phi);
            gcd = extended_euclidean_algorithm(key.e, key.phi, x, y);
        }

        key.d = x;

        self.key = key;

        return key;
    }
}
