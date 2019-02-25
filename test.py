import tensorflow as tf

mnist = tf.keras.datasets.mnist
model = tf.keras.models.load_model("/models/epicmodel.model")

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = tf.keras.utils.normalize(x_test, axis=1)

val_loss, val_acc = model.evaluate(x_test, y_test)

print(val_loss)
print(val_acc)
