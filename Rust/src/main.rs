mod RSA;

fn main()
{
    let mut k = RSA::RSAKey::create();
    println!("Value is: {num}", num = RSA::algor::random_num(0u32, 100u32));
}
