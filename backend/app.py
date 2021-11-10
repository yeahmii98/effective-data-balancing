import os
import json
from flask import Flask, request, render_template
from werkzeug import secure_filename

app = Flask(__name__)


@app.route("/getPlateDetection", methods=["GET"])
def get_plate_detection():
    file_name = request.args["file_name"]
    if file_name:
        with open("test_sample/detection_sample.json", "r", encoding="utf-8") as j:
            result = json.load(j)
        return result
    else:
        return "sample output"


@app.route("/showImg")
def showImg():
    return render_template("showImg.html")


@app.route("/fileUpload", methods=["POST"])
def file_upload():
    file = request.files["file"]
    file.save(os.path.join("test_sample", secure_filename(file.filename)))  # s3
    return "file uploaded"


@app.route("/getClassification/")
def get_classification():
    return "Return sample"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
