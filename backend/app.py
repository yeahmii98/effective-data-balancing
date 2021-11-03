import os
import json
from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)


@app.route("/getDetection", methods=["GET"])
def get_detection():
    file_name = request.args["file_name"]
    if file_name:
        with open("test_sample/detection_sample.json", "r", encoding="utf-8") as j:
            result = json.load(j)
        return result
    else:
        return ""


@app.route("/fileUpload", methods=["POST"])
def file_upload():
    file = request.files["file"]
    file.save(os.path.join("test_sample", secure_filename(file.filename)))  # s3
    return "file uploaded"


@app.route("/getClassification/")
def get_classification():
    return "Return sample"


if __name__ == "__main__":
    app.run(debug=True)
    # 디버그 모드. 변경을 자동으로 감지하여 리로드하며 디버거를 제공한다. 운영 환경에서는 절대 사용 금지!
