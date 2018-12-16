

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    print("file request ::", request.files)

    allfiles = request.files.getlist('file')
    if 'file' not in request.files:
        return "No file found"
    for file in allfiles:
        print(file)
        file.save("static/" + file.filename)

    #file = request.files['file']
    #print("all file ::", file)

    return "file successfully saved"


if __name__ == '__main__':
    app.run(port=8081,debug=True)