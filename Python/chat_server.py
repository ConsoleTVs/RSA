# Copyright (c) 2019 Erik Campobadal Fores <soc@erik.cat>
# Distributed under the MIT License

from sys import exit
from socket import socket, SHUT_RDWR
from threading import Thread

# Start a socket instance
sk = socket()
# Bind the socket to a given IP and PORT
sk.bind(('127.0.0.1', 8000))
# Start listening for incomming connections
sk.listen(1)
# Helper function
def log(message, arrow = True):
    print(('-> ' if arrow else '') + message)

# Output a message
print('Copyright (c) 2019 Erik Campobadal Fores <soc@erik.cat>\n')
log('[Info] Listening on 127.0.0.1:8000')

# Stores the current connections.
connections = []

def entry(conn, addr):
    global connections
    connections.append(conn)
    log('[Connected] ' + addr[0] + ':' + str(addr[1]))
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                raise Exception("Client disconnected")
            msg = str(addr[0]) + ':' + str(addr[1]) + ' - ' + data.decode("utf-8")
            log(msg)
            for c in connections:
                if c != conn: c.send(bytes(msg, 'utf-8'))
        except:
            conn.shutdown(SHUT_RDWR)
            log('[Disconected] ' + str(addr[0]) + ':' + str(addr[1]))
            if conn in connections:
                connections.remove(conn)
            exit()

# Start listening for connections.
while True:
    try:
        conn, addr = sk.accept()
        thread = Thread(target = entry, kwargs = {'conn': conn, 'addr': addr})
        thread.daemon = True
        thread.start()
    except:
        log('[Closing] Aborting sockets...')
        sk.shutdown(SHUT_RDWR)
        exit()
