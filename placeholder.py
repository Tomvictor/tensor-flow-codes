import tensorflow as tf 



print("Starting....")
sess = tf.Session()
# define placeholders
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# define addition shortcut or addition node
adder_node = a + b

print(sess.run(adder_node,{a:3,b:4.5}))
print(sess.run(adder_node,{a:[1,3],b:[2,4]}))

add_and_triple = adder_node * 3

print(sess.run(add_and_triple,{a:3,b:4.5}))