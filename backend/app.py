import os
import requests
import s3_access
from flask import Flask, request
from werkzeug import secure_filename
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
bucket = s3_access.get_s3_bucket()


@app.route("/healthcheck/")
def health_check():
    return "200 OK"


@app.route("/getPlateDetection", methods=["GET"])
def get_plate_detection():
    file_name = request.args["file_name"]
    params = {"source": file_name}
    URL = os.getenv("PLATE_DETECTION_URL")
    response = requests.get(URL, params)
    return response.text  # s3 endpoint 전달? 아니면 img 다운로드 후 binary file 전달?


@app.route("/fileUpload", methods=["POST"])
def file_upload():
    file = request.files["file"]
    file.save(secure_filename(file.filename))
    s3_access.upload_file(bucket, file.filename, file.filename)
    return "file uploaded"


@app.route("/getClassification/")
def get_classification():
    return "Return sample"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
