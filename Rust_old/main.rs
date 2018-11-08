mod RSA;

fn main()
{
    let mut k = RSA::RSAKey::create();
    println!("Value is: {num}", num = RSA::algor::num_bits(255u128));
}
