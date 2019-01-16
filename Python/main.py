from RSACryptosystem import RSA

# Initiate the RSA cryptosystem
system = RSA()

# You may also provide two parameters
# p, q to the generate_key() function.
key = system.generate_key()
# This will print to the screen a key representation.
key.print()
# The message to be encrypted
message = 'Cryptography'
print(f'Original: {message}')
# The resulting cipher text of
# encrypting the original message
cipher_text = system.encrypt(message)
print(f'Cipher text: {cipher_text}')
# The resulting plain text after
# decrypting the cipher text recieved
plain_text = system.decrypt(cipher_text)
print(f'Plain text: {plain_text}')
# Simple check to see if they match
print(f'Correct: {message == plain_text}')
