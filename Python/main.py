from RSA.RSA import RSA

system = RSA()

key = system.generate_key(61, 53)
key.print()

message = 'Cryptography'
cipher_text = system.encrypt(message)
plain_text = system.decrypt(cipher_text)
print(f'Original: {message}')
print(f'Cipher text: {cipher_text}')
print(f'Plain text: {plain_text}')
print(f'Correct: {message == plain_text}')
