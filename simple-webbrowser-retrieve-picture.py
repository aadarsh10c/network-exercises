#retireve image from the webserver and store it in a file:
import socket
#import time

HOST='data.pr4e.org'
PORT=80

count=0
picture=b'' #data transfer takes place in bytes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
    while True:
        data=s.recv(5120)
        if len(data) > 0:
            count=count +len(data)
            print(len(data),count)
            picture+=data
            #time.sleep(1)
            
        else:
            break
             
#print header
pos=picture.find(b'\r\n\r\n')
print(picture[:pos])

#store the image
image=picture[pos+4:]

with open('stuff.jpg','wb') as f:
    f.write(image)
