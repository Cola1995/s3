import  socket

sk=socket.socket()
sk.connect(("127.0.0.1",8087))
data=sk.recv(1024).decode("utf-8")
print(data)
msg=input(">>>").encode('utf-8')
sk.send(msg)
sk.close()