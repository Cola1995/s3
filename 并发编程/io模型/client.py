import time
import socket
import threading
def func():
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    sk.send(b'hello')
    time.sleep(1)
    print(sk.recv(1024))
    sk.close()

for i in range(2):
    threading.Thread(target=func).start()