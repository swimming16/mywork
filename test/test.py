import pandas as pd
import numpy as np
import tensorflow as tf

# table =pd.DataFrame(
# #     np.random.rand(6, 4), columns=['a', 'b', 'c', 'd']
# # )
# # print(table)
# # print(table.loc[1, 'a'])
# # print(table.idxmax())
# # print(table.idxmax(1,))


a=np.random.rand(6,4)
#l=np.argmax(a)
print(a)
print(a[:,:2])
#print(l)
# w1=tf.Variable(tf.random_normal([2,3]))
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(tf.random_uniform(
#         (2,4), -1.0, 1.0)))
#     print (sess.run(w1))
    #print(sess.run(tf.Variable(tf.random_normal_initializer(0, 0.3))))


############ 如何打印一个tf变量
# biases = tf.Variable(tf.zeros([1, 5]) + 0.1)
# init=tf.initialize_all_variables()
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(biases))