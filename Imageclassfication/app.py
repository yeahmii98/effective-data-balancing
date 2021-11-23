import torch
import classfication
#from torchvision import transforms
from flask import Flask, request
import os
#from efficientnet_pytorch import EfficientNet
#model = EfficientNet.from_pretrained('efficientnet-b0')
#torch.save(model,'classfications')
app = Flask(__name__)


@app.route("/",methods=["GET"])
def main():
    source = request.args["source"]
    with torch.no_grad():
        response = classfication.classfy(source=source)
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)


