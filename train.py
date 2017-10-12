import tensorflow as tf 

print("Starting...")
sess = tf.Session()
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
# print(linear_model)
#variables will never initialized until we run the call below
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model,{x:[1,2,3,4]}))

# loss function
# Aloss function measures how far apart the current model is from the provided data
# which is the sum of the deltas between the current model and the provided data
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

# changing the variable default values
fixW = tf.assign(W,[-1.])
fixb = tf.assign(b,[1.])
sess.run([fixW,fixb])
print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
#reseting the values to default
sess.run(init)
for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

print(sess.run([W,b]))


