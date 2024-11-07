# ultralytics

## 使用流程

### 添加模型架构描述文件

在 [ultralytics/cfg/models](./ultralytics/cfg/models) 目录下创建模型架构描述文件(`.yaml`)即可。

注意事项:

- [ultralytics/cfg/models](./ultralytics/cfg/models) 目录和其子目录下的 `.yaml` 文件**不能重名**，因为默认会使用 `glob.glob(str(ROOT / "**" / file), recursive=True)` 搜索
- 模型架构描述文件的命名要符合规范，尽量按照 `yolo[v]?\d+([nslmx])` 的规则命名，因为 `guess_model_scale()` (定义在[tasks.py](./ultralytics/nn/tasks.py))方法会根据 `.yaml` 文件的名称去猜测使用多大尺寸的模型(`nslmx`)


### 添加数据集描述文件

在 [dataset](./dataset) 目录下创建数据集描述文件(`.yaml`)即可。

### 训练模型

```shell
python train.py --cfg [model.yaml] --data [dataset.yaml]
```



