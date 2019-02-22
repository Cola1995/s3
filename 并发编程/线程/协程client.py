import socket


sk=socket.socket()

sk.connect(("127.0.0.1",8089))

print(sk.recv(1024))

msg=input(">>>").encode("utf-8")
sk.send(msg)
sk.close()