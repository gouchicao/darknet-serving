# darknet-serving
> 基于darknet的模型服务器

## 构建darknet-serving镜像（GPU）
```bash
docker build -t darknet-serving:latest-gpu .
```

## 运行darknet-serving容器（GPU）
* 使用你的模型绝对路径替换$model_dir
```bash
docker run --runtime=nvidia -it --name=darknet-serving \
    --volume=$model_dir:/darknet-serving/model \
    darknet-serving:latest-gpu
```