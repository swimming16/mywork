# 导入socket模块
import socket
# 创建socket对象,默认参数就不填了
sock = socket.socket()
# 绑定IP和端口,参数是一个元组(ip,port)
sock.bind(('127.0.0.1', 8080))
# 开始监听,最大监听数为5
sock.listen(5)
# 阻塞,等待连接,返回一个链接通道和一个地址
conn,addr = sock.accept()
# 接收请求数据,接收大小为1024字节
content = conn.recv(1024)
print(addr)#得到地址和端口号
# 打印结果(bytes转成str显示)
print(content.decode())
# 发送请求结果,必须以bytes类型
conn.send(b'Hello 2222')
# 关闭链接c
conn.close()
# 关闭套接字
sock.close()