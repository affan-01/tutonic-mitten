from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
from encrypt import encrypt_file 
from decrypt import decrypt_file

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/upload' , methods = ['GET' , 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        encrypt_file(f.filename)
        with open('static/filekey','r') as filekey:
            key = filekey.read()
        return render_template('acknowledgment.html' , key = key)


@app.route('/download' , methods = ['GET' , 'POST'])
def download():
    if request.method == "POST":
        input_key = request.form.get('key')
    with open('static/filekey','r') as filekey:
        key = filekey.read()
    if input_key == key:
        return decrypt_file(key)
    


if __name__ == "__main__":
    app.run(debug="True")