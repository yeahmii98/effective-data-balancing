import set_weights

set_weights.get_files()

import detect_image
from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    file_name = request.args["file_name"]
    response = detect_image.run_demo(file_name)
    return response


@app.route("/fileUpload", methods=["POST"])
def file_upload():
    file = request.files["file"]
    file.save(secure_filename(file.filename))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
