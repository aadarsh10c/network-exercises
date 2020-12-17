import socket

HOST="data.pr4e.org"
PORT=80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    cmd=b"GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n"
    s.send(cmd)
    while True:
        data = s.recv(512)
        if len(data) < 1:
            break
        print(data.decode())    
