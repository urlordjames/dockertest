import tensorflow as tf
  
mnist = tf.keras.datasets.mnist #images of hand drawings

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

asdasdasdhiausdbasda;a;sdhub #attempt to trigger circleci fail

model.compile(optimizer="nadam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"])

model.fit(x_train, y_train, epochs=3)

model.save("/models/epicmodel.model")
