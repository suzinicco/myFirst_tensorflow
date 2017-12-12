import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a,b)

sess = tf.Session()

print sess.run(y,feed_dict={a:3, b:3})

## git commit test

print ("hello world")


## git commit test 2

print ("hello git")

## git commit test 3

print ("hello git bro")

## git commit test 4

print ("commit test 4")

## git commit test 5

print ("commit test 5")

print ("commtit test 6")

print ("commit test 77777")

print ("commit test 8888")