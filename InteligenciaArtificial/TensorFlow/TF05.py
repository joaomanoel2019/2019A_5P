# codigo original - Machine Learning with TensorFlow
# 2019-05-17
# @gustavopoli
# --------------------------------------
# Listing 2.7 Using the interactive session mode

import tensorflow as tf

sess = tf.InteractiveSession()

x = tf.constant([[1., 2.]])
neg_op = tf.negative(x)

print(x)
print(neg_op)

result = neg_op.eval()

print(result)

sess.close()

print("..| end application")

