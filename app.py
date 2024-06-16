from flask import Flask,render_template,url_for,request
from urllib.request import urlopen
from PIL import Image
from keras.preprocessing import image 
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == "POST":
		url = request.form['url']
		if url:			
			img = Image.open(urlopen(url))
			img = img.resize((28,28))
			img = np.array(image.img_to_array(img))
			img = img[:,:,0]
			img = img.reshape(1,28,28)
			# plt.matshow(img[0])
			# plt.show()
			cnn = tf.keras.models.load_model('mnist.keras')
			y_pred = cnn.predict(img)
			value = np.argmax(y_pred, axis=1)
			l = []
			for i in range(10):
				l.append(y_pred[0][i]*100)
			return render_template('home.html', url = url, ans = l, value = value[0])
		else:
			return render_template('home.html')
	else:
		return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)