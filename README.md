# darknet-serving
> 基于darknet的模型服务器

## 获得darknet-serving镜像（GPU）
> 有两种方式：拉取hub.docker上的镜像和自己在本地生成镜像。

### 1. 拉取darknet-serving镜像
```bash
$ sudo docker pull gouchicao/darknet-serving:latest-gpu
```

### 2. 构建darknet-serving镜像
```bash
$ sudo docker build -t darknet-serving:latest-gpu .
```

## 准备您的模型
* 模型目录结构
    ```
    model   　　　　　　　　　　模型目录
    ├── voc.data　　　　　　   配置文件
    ├── voc.names　　　　　　  标签名
    ├── yolov3.cfg　　　　　   YOLOv3神经网络文件
    └── yolov3_final.weights 模型的权重值
    ```

* 编辑voc.data
    ```
    classes= 2
    names = model/voc.names
    ```

## 运行模型预测服务
> 使用你的模型绝对路径替换$model_dir
```bash
$ sudo docker run --runtime=nvidia -it --name=darknet-serving \
    --volume=$model_dir:/darknet-serving/model \
    darknet-serving:latest-gpu
```
