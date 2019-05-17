# codigo original - Machine Learning with TensorFlow
# 2019-05-17
# @gustavopoli
# --------------------------------------
# Listing 2.5 Using the negative operator

import tensorflow as tf

x = tf.constant([[1, 2]])

neg_x = tf.negative(x)

print(x)
print("---")
print(neg_x)

print("..| end application")


