import tensorflow as tf
import numpy as np

# 使用 Numpy 生成假的數據，x_data為numpy的陣列裡面有2x100個隨機浮點數，代表100組(w, b)
x_data = np.float32(np.random.rand(2, 100))
# y_data是 將x_data丟入正確模型所產生的正確結果，一樣是100組
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# 建構一個線性模型
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化平方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化變數
init = tf.global_variables_initializer()

# 啟動圖(graph)
sess = tf.Session()
sess.run(init)

# 利用graph學習模型
for step in range(0, 121):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
