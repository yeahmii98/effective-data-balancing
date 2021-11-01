from flask import Flask

app = Flask(__name__)


@app.route("/getDetection/")
def get_detection():
    return "Return Detection Result"


@app.route("/getClassification/")
def get_classification():
    return "Return Classification Result"


if __name__ == "__main__":
    app.run(debug=True)
    # 디버그 모드. 변경을 자동으로 감지하여 리로드하며 디버거를 제공한다. 운영 환경에서는 절대 사용 금지!
