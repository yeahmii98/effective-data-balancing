import json
from PIL import Image
import torch
import s3_access
from torchvision import transforms
from flask import Flask, request
import os
app = Flask(__name__)


def classfy(source=None, save_img=True):
    source_bucket = s3_access.get_s3_bucket()

    file_path = os.path.join('Imageclassfication', source)
    s3_access.download_file(source_bucket, source, file_path)

    model = torch.load('./Imageclassfication/' + 'classfications')
    # source = img.jpg
    Model_input_image = file_path

    # Preprocess image
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

    #json
    save_dict = {"result": {"classfy": [], "conf": []}}
    for idx in torch.topk(outputs, k=1).indices.squeeze(0).tolist():
        object_dict = {}
        object_dicts = {}
        prob = torch.softmax(outputs, dim=1)[0, idx].item()
        object_dict[idx] = '{label:<1}'.format(label=labels_map[idx])
        object_dicts[idx] = '{p:.2f}%'.format(p=prob * 100)
        save_dict["result"]["classfy"].append(object_dict[idx])
        save_dict["result"]["conf"].append(object_dicts[idx])
        # print('{label:<75} ({p:.2f}%)'.format(label=labels_map[idx], p=prob * 100))
    json_file_name = "classfy" + "_output.json"
    json_save_path = os.path.join('Imageclassfication',json_file_name)
    with open(json_save_path, "w", encoding="utf-8") as f:
        json.dump(save_dict, f, ensure_ascii=False)


    client = s3_access.get_s3_client()
    #인풋이미지와 아웃풋이미지가 같아서 같이썼음
    #file_path= /Imageclassfication/img.jpg
    output_file_name = file_path
    s3_access.upload_file(source_bucket, file_path, output_file_name)
    s3_access.upload_file(source_bucket, json_save_path, json_file_name)

    res_json = {
        "img_url": s3_access.get_public_url(client, file_path),
        "json_url": s3_access.get_public_url(client, json_file_name),
        "text_arr": res_label,
    }
    # file_path= /Imageclassfication/img.jpg
    return output_file_name