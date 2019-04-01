import numpy as np
import tensorflow as tf

############    Session
mat1=np.arange(6).reshape(2,3)
mat2=np.arange(9).reshape(3,3)
print(mat1)
print(mat2)

# print(np.dot(mat1,mat2))
# matrix1 = tf.constant(mat1)
# matrix2 =tf.constant(mat2)
#
# result=tf.matmul(matrix1,matrix2)
#
# with tf.Session() as sess:
#     print(sess.run(result))

############   tf.Vaiable()
# a=tf.Variable(mat1)
# b=tf.Variable(mat2)
#
# result=tf.matmul(a,b)
#
# init = tf.initialize_all_variables()#初始化变量
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(result))
############  tf,placeholder()
input1=tf.placeholder(tf.int32)
input2=tf.placeholder(tf.int32)
output=tf.matmul(input1,input2)
with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:mat1,input2:mat2}))

############ 如何打印一个tf变量
# biases = tf.Variable(tf.zeros([1, 5]) + 0.1)
# init=tf.initialize_all_variables()
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(biases))


