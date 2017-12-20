import tensorflow as tf
hello  = tf.constant("Hello, TensorFlw!")

sess = tf.Session()

print(sess.run(hello))

