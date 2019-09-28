from socket import socket, AF_INET, SOCK_STREAM
from clientconfig import serverhost, serverport

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverhost, serverport))

while True:
    try:
        send_text = input("client => ").strip()
    except Exception as e:
        print(e)
        sock.close()
        exit(-1)
    if not send_text:
        break
    send_data = send_text.encode()
    sock.send(send_data)
    recv_data = sock.recv(1024)
    print("server => {}".format(recv_data.decode()))

sock.close()