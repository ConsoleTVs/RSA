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
