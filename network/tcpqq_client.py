import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 8080))
# 实现通信循环
while True:
    messages = input("Please input your messages to be sent:").strip().encode('utf-8')
    # 注意发送的内容不能为空,否则接收方就会一直等下去
    if not messages:
        print("Can't be empty...")
        continue
    elif messages == b'q':
        break
    else:
        sock.send(messages)
        data = sock.recv(1024)
        print("Messages from [{}]:{}".format(('127.0.0.1', 8080), data.decode('utf-8')))
sock.close()