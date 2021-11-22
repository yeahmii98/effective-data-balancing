import PIL.Image
import cv2
import torch
from PIL import Image
import boto3
import os
import pandas as pd
import s3_access
from flask import Flask, request
from pathlib import Path
app = Flask(__name__)
import json

@app.route("/",methods=["GET"])
def main():
    #source=image0.jpg
    #1.s3에 업로드 된 파일 이름
    source = request.args["source"]

    #2.s3버켓 객체 받아오기
    source_bucket = s3_access.get_s3_bucket()
    #3.s3이미지 받아와서 로컬에 저장할 경로
    file_path = os.path.join("/test",source)
    #4.s3에서 받아오고 로컬에 저장
    s3_access.download_file(source_bucket,source,file_path)
    #5.저장된 이미지로 모델 업로드 및 실행
    model = torch.load('./' + 'Detection_model.pt')
    Model_input_image = [file_path]
    results = model(Model_input_image, size=640)

    path, filename = "/test" , "image0.jpg"
    #6.파일경로와 확장자 분리 origin_name = /test/image0
    origin_name, ext = os.path.splitext(filename)
    #7.모델 결과 저장할 경로 지정 및 저장
    output_file_name = origin_name + "_output" + ext
    model_output_save_path = os.getcwd()
    output_save_path=os.getcwd()+"/image0.jpg"
    results.save(model_output_save_path)

    #8.json형식 아웃풋 저장 변수
    json_input_data = results.pandas().xyxy[0]
    # orient index
    #9.json 저장 파일 경로지정.
    json_file_name = origin_name + "_output.json"
    #10.json 파일로 저장
    json_input_data.to_json(json_file_name, orient='table')
    json_save_path = os.path.join(path, json_file_name)

    s3_access.upload_file(source_bucket, output_save_path, output_file_name)
    s3_access.upload_file(source_bucket, json_save_path, json_file_name)

    s3_access.get_public_url
    return "z"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)

#model = torch.load('./'+'Detection_model.pt')
#print(type(model))
# 모델에 넣을 이미지 가져오기
# 현재 디렉토리에 샘플이미지가 존재함.
# 샘플이미지 제거 후 input이미지에 맞게 조정 필요!!!
#Model_input_image1 = Image.open('images.jpg')  # PIL image
#Model_input_image2 = cv2.imread('bus.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)
#Model_input_image= [Model_input_image2] # batch of images

# Inference
#results = model(Model_input_image, size=640)  # includes NMS
# Results
#results.print()

#results.xyxy[0]  # img1 predictions (tensor)
#xyxy 이미지 배열 순 좌표값 출력
#ex xyxy[0] -> 첫번째이미지
#xyxy[1] -> 두번째이미지
#print(results.pandas().xyxy[1]) # img1 predictions (pandas)
#json_input_data = results.pandas().xyxy[0]
#orient index
#json_input_data.to_json('TofrontEnd.json',orient='table')


#AWS_S3_CREDS = {
#         "aws_access_key_id" : os.environ.get("aws_access_key_id"),
#         "aws_secret_access_key" : os.environ.get("aws_secret_access_key")
#}

#s3 = boto3.client('s3',**AWS_S3_CREDS)
#filename = 'TofrontEnd.json'
#bucket_name = 'kdgec2s3'
#정보확인

#s3.upload_file(filename,bucket_name,filename)
# 첫본째 매개변수 : 로컬에서 올릴 파일이름
# 두번째 매개변수 : S3 버킷 이름
# 세번째 매개변수 : 버킷에 저장될 파일 이름.

#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie