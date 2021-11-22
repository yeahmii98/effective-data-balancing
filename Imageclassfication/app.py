import json
from PIL import Image
import torch
import s3_access
from torchvision import transforms
from flask import Flask, request
import os
from efficientnet_pytorch import EfficientNet
#model = EfficientNet.from_pretrained('efficientnet-b0')
#torch.save(model,'classfications')
app = Flask(__name__)


@app.route("/",methods=["GET"])
def main():
    # 1.s3에 업로드 된 파일 이름
    source = request.args["source"]
    # 2.s3버켓 객체 받아오기
    source_bucket = s3_access.get_s3_bucket()
    #4.s3에서 받아오고 로컬에 저장
    # source = img.jpg
    file_path = os.path.join('sample', source)
    s3_access.download_file(source_bucket,source,file_path)
    #5.저장된 이미지로 모델 업로드 및 실행
    model = torch.load('./' + 'classfications')
    # source = img.jpg

    Model_input_image = file_path

    # Preprocess image
    # 평균과 표준(이미지에 대한)

    tfms = transforms.Compose([transforms.Resize(224), transforms.ToTensor(),
                               transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]), ])

    # Image.open('./sample/img.jpg')
    img = tfms(Image.open(Model_input_image)).unsqueeze(0)
    # print(img.shape) # torch.Size([1, 3, 224, 224])

    # Load ImageNet class names
    labels_map = json.load(open('./sample/labels_map.txt'))
    labels_map = [labels_map[str(i)] for i in range(1000)]

    # Classify
    model.eval()
    with torch.no_grad():
        outputs = model(img)

    # Print predictions
    print('-----')
    for idx in torch.topk(outputs, k=1).indices.squeeze(0).tolist():
        prob = torch.softmax(outputs, dim=1)[0, idx].item()
        print('{label:<75} ({p:.2f}%)'.format(label=labels_map[idx], p=prob * 100))

    return "hi"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)


