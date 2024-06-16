import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"

import tensorflow as tf
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

cnn = tf.keras.models.load_model('mnist.keras')

(X_train, y_train), (X_test, y_test) = mnist.load_data()

y_pred = cnn.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)

from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))
