import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()
conn_l = []
del_conn = []
while True:
    try:
        conn,addr = sk.accept()  #不阻塞,但是没人连我会报错
        print('建立连接了:',addr)
        conn_l.append(conn)
    except BlockingIOError:
        for con in conn_l:
            try:
                msg = con.recv(1024)  # 非阻塞,如果没有数据就报错
                if msg == b'':
                    del_conn.append(con)
                    continue
                print(msg)
                con.send(b'byebye')
            except BlockingIOError:pass
        for con in del_conn:
            con.close()
            conn_l.remove(con)
        del_conn.clear()
# while True : 10000   500  501

