# darknet-serving
> 基于darknet的模型服务器

## 获得darknet-serving镜像（GPU）
1. 拉取Docker Hub上的darknet-serving镜像
```bash
$ sudo docker pull gouchicao/darknet-serving:latest-gpu
```

2. 自己构建darknet-serving镜像
```bash
$ sudo docker build -t darknet-serving:latest-gpu .
```

## 运行模型预测服务
1. 使用绑定挂载点
```bash
# 使用您本机的绝对路径设置model_dir
$ model_dir=/home/wjunjian/github/gouchicao/darknet/model-zoo/platen-switch/model

# 部署模型
$ sudo docker run --runtime=nvidia -it --name=darknet-serving \
    --volume=$model_dir:/model \
    darknet-serving:latest-gpu
```

2. 使用存储卷
```bash
# 创建存储卷
$ sudo docker run --name darknet-model-platen-switch --volume /model \
    gouchicao/darknet-model-platen-switch:latest

# 部署模型
$ sudo docker run --runtime=nvidia -it --name=darknet-serving-platen-switch -p 7713:7713 \
    --volumes-from darknet-model-platen-switch \
    gouchicao/darknet-serving:latest-gpu
```
