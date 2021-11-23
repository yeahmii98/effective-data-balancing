
import torch
import os
import s3_access
from flask import Flask, request

app = Flask(__name__)


def detect(source=None, save_img=True):
    source_bucket = s3_access.get_s3_bucket()
    # 3.s3이미지 받아와서 로컬에 저장할 경로 이미지 만들 때
    file_path = os.path.join("/app", source)

    # 4.s3에서 받아오고 로컬에 저장
    s3_access.download_file(source_bucket, source, file_path)

    # 5.저장된 이미지로 모델 업로드 및 실행
    model = torch.load('./' + 'Detection_model.pt')
    Model_input_image = [file_path]
    results = model(Model_input_image, size=640)

    path, filename = "/app", "image0.jpg"
    # 6.파일경로와 확장자 분리 origin_name = /test/image0
    origin_name, ext = os.path.splitext(filename)

    # 7.모델 결과 저장할 경로 지정 및 저장
    output_file_name = origin_name + "_output" + ext
    model_output_save_path = os.getcwd()
    output_save_path = os.getcwd() + "/image0.jpg"
    results.save(model_output_save_path)

    # 8.json형식 아웃풋 저장 변수
    json_input_data = results.pandas().xyxy[0]

    # 9.json 저장 파일 경로지정.
    json_file_name = origin_name + "_output.json"
    # 10.json 파일로 저장
    json_input_data.to_json(json_file_name, orient='table')
    json_save_path = os.path.join(path, json_file_name)

    client = s3_access.get_s3_client()
    s3_access.upload_file(source_bucket, output_save_path, output_file_name)
    s3_access.upload_file(source_bucket, json_save_path, json_file_name)

    res_json = {
        "img_url": s3_access.get_public_url(client, output_file_name),
        "json_url": s3_access.get_public_url(client, json_file_name),
        "text_arr": res_label,
    }


    return output_file_name
