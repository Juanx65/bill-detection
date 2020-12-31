from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

imagesFolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] = imagesFolder

from commons import detection_on_image, convertir_divisas

@app.route('/', methods=['GET','POST'])
def predict():

	if request.method=='GET':
		img1 = os.path.join(app.config['UPLOAD_FOLDER'],'capturando.png')
		return render_template('index.html', user_image = img1)

	if request.method=='POST':
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
		div_in = request.form['div_in']
		div_out = request.form['out']
		image = file.read()
		#try:
		result, cant_total = detection_on_image(image)
		#except:
		#	return render_template('handler.html',error = "Can't upload image" )

		cant_out = convertir_divisas(cant_total,div_in,div_out)

		return render_template('result.html',result = result,cant_total = cant_total,div_out = div_out, cant_out = cant_out, div_in = div_in)

@app.route('/aboutapp.html', methods=['GET'])
def aboutapp():
    return render_template('aboutapp.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)#host='0.0.0.0'
