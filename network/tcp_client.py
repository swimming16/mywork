# 导入socket模块
import socket
# 创建socket对象
sock = socket.socket()
# 建立链接
sock.connect(('127.0.0.1', 8080))
# 发送请求数据,必须以bytes类型
sock.send(b"I'm Lyonlll")
# 接收请求结果
content = sock.recv(1024)
# 打印结果
print(content.decode())
# 关闭套接字
sock.close()