from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

UPLOAD_FOLDER = 'templates'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from commons import get_detection, convertir_divisas

@app.route('/', methods=['GET','POST'])
def predict():

	if request.method=='GET':
		return render_template('index.html')

	if request.method=='POST':
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
		div_in = request.form['div_in']
		div_out = request.form['out']
		image = file.read()
		try:
			result, cant_total = get_detection(image)
		except:
			return render_template('handler.html',error = "can't upload image" )

		cant_out = convertir_divisas(cant_total,div_in,div_out)
		return render_template('result.html',result = result,cant_total = cant_total,div_out = div_out, cant_out = cant_out, div_in = div_in)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/show/flechaback.png')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/templates/' + filename
    return render_template('result.html', filename=filename)

@app.route('/uploads/flechaback.png')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, flechaback.png)


if __name__ == '__main__':
	app.run(host='0.0.0.0')#host='0.0.0.0'
