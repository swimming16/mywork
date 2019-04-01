import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def add_layers(inputs,in_size,out_size,activation_function=None):
    Weights =tf.Variable(tf.random_normal([in_size,out_size]))
    biases =tf.Variable(tf.zeros([1,out_size]))
    result =tf.matmul(inputs, Weights)+biases
    if activation_function is None:
        output=result
    else:
        output = activation_function(result)
    return output

x_data=np.linspace(1,10,300)[: ,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=x_data*2+noise

xs =tf.placeholder(tf.float32, [None,1])#None暂时不清楚维度，可以为任意数
ys=tf.placeholder(tf.float32, [None,1])

l1=add_layers(xs,1,10,activation_function=tf.nn.relu)
prediction=add_layers(l1,10,1, activation_function=None)

loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
train=tf.train.GradientDescentOptimizer(0.1).minimize(loss)


init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ylim([0,30])
plt.ion()
plt.show()

for i in range(1000):
    sess.run(train,feed_dict={xs:x_data,ys:y_data})
    print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
    # print(sess.run(prediction, feed_dict={xs: x_data, ys: y_data}))
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(1)



