# ultralytics


## 使用流程

### 1 添加模型架构描述文件

在 [cfg](./cfg) 目录下创建模型架构描述文件(`.yaml`)即可。

注意事项:

- 模型架构描述文件的命名要符合规范，尽量按照 `yolo[v]?\d+([nslmx])` 的规则命名，因为 `guess_model_scale()` (定义在[tasks.py](./ultralytics/nn/tasks.py))方法会根据 `.yaml` 文件的名称去猜测使用多大尺寸的模型(`nslmx`)


### 2 添加数据集描述文件

在 [dataset](./dataset) 目录下创建数据集描述文件(`.yaml`)即可。

### 3 训练模型

> [train.py](./train.py) 仅供 Debug 使用, 训练 YOLO 模型建议使用如下命令行工具

各参数的含义具体见 [ultralytics train-settings](https://docs.ultralytics.com/modes/train/#train-settings)

```shell
yolo detect train \
data=[DATASET.yaml] \
model=[MODEL.yaml] \
epochs=300 \
imgsz=640 \
batch=32 \
name=[MODEL NAME]
```

使用 tensorboard 查看训练过程模型的性能变化曲线

```shell
tensorboard --host 0.0.0.0 --port 8000  --logdir runs/detect/[MODEL NAME]
```

### 4 评估模型

训练模型结束时输出的是在验证集上的性能，使用如下命令评价模型在测试集上的性能

```shell
yolo val \
data=[DATASET.yaml] \
model=runs/detect/[MODEL NAME]/weights/best.pt \
split=test \
imgsz=640 \
batch=32
```
