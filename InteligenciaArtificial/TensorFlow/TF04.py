# codigo original - Machine Learning with TensorFlow
# 2019-05-17
# @gustavopoli
# --------------------------------------
# Listing 2.6 Using a session

import tensorflow as tf

x = tf.constant([[1., 2.]])
neg_op = tf.negative(x)

print(x)
print(neg_op)

with tf.Session() as sess:
    result = sess.run(neg_op)

print(result)

print("..| end application")

