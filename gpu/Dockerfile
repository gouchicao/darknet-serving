FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04
LABEL maintainer="wang-junjian@qq.com"

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nano \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /darknet-serving/
WORKDIR /darknet-serving
RUN pip3 install --no-cache-dir -r requirements.txt

ADD *.py /darknet-serving/
ADD ./gpu/libdarknet.so /darknet-serving/

EXPOSE 7713

ENTRYPOINT ["python3", "darknet_model_server.py"]

