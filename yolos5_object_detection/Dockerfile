FROM brunneis/python:3.8.6-ubuntu-focal@sha256:fe3ac7d68746bebd16f7c7ccd93f049c19354d297673ce0c3d5c59cad890b7a2
COPY /yolos5_object_detection/   /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip gfortran libopenblas-dev liblapack-dev
RUN pip install --upgrade pip
RUN pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

RUN pip install -r /test/requirements.txt