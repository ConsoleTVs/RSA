# Copyright (c) 2019 Erik Campobadal Fores <soc@erik.cat>
# Distributed under the MIT License
from RSACryptosystem import RSA
from threading import Thread
from socket import socket, SHUT_RDWR
from time import sleep

# Start a socket instance
sk = socket()
# Connect to a given IP and PORT
sk.connect(('127.0.0.1', 8000))
# Output a message
print('Copyright (c) 2019 Erik Campobadal Fores <soc@erik.cat>\n')
print("Conencted at 127.0.0.1:8000")
# RSA cryptosystem
rsa = RSA()
# Print the refence key
rsa.generate_key().print()
# Stores the RSA keys
keys = []

# Listener function for the thread
def listener():
    global sk
    while True:
        try:
            data = sk.recv(1024)
            if not data:
                raise Exception("Client disconnected")
            msg = data.decode("utf-8")
            raw = msg[msg.find(' - ') + 3:]
            if raw[0] == '[' and raw[len(raw) - 1] == ']':
                cipher = raw[1:len(raw) - 1].replace(' ', '')
                cipher = [int(i) for i in cipher.split(',')]
                print(msg[:msg.find(' - ') + 3] + rsa.decrypt(cipher))
            elif raw[:3] == 'K: ':
                key = raw[3:]
                e = int(key[:key.find(' ')])
                n = int(key[key.find(' ') + 1:])
                keys.append((e, n))
                print(f'[RSA] Key set for {len(keys) - 1} with e = {e} and n = {n}')
            else: print(msg)
        except Exception as e:
            print(e)
            sk.shutdown(SHUT_RDWR)
            exit()

# Start the listener thread.
Thread(target = listener).start()

while True:
    num = input()
    if num[:4] == 'K: A':
        num = f'K: {rsa.key.e} {rsa.key.n}'
    if num[:3] == "E: ":
        begin = num.find(' ', 4)
        index = int(num[3:begin])
        if index >= 0 and index < len(keys):
            # Encrypt the message
            num = str(rsa.encrypt(num[begin + 1:], keys[index][0], keys[index][1]))
    sk.sendall(bytes(num, 'utf-8'))
    sleep(1)
