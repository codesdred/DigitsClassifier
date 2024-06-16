import tensorflow as tf
from keras.datasets import mnist
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()

from keras.models import Sequential
cnn = Sequential()
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
cnn.add(Conv2D(filters = 32, kernel_size = 3, activation = 'relu', input_shape = [28,28,1]))
cnn.add(MaxPool2D(pool_size = 2, strides = 2))
cnn.add(Flatten())
cnn.add(Dense(units = 10, activation = 'softmax'))
cnn.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
cnn.fit(X_train, y_train, batch_size = 32, epochs = 5)

print(cnn.summary())

cnn.save('mnist.keras')

