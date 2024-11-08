# YOLO Configuration

该目录存放 YOLO 模型配置文件：

- 带有 `origin` 后缀的 YAML 文件是 Ultralytics 提供的官方配置文件，拷贝自 [ultralytics/cfg/models/](../ultralytics/cfg/models/) 目录。
- 其他配置文件为自定义配置文件或修改自官方配置文件, 要求名称中具备版本号

版本号规范(`v<major>.<minor>.<patch>`):

- `<major>`: 大幅度更改模型结构
- `<minor>`: 简单更改模型结构, 比如替换/删除某一层等
- `<patch>`: 未更改模型结构, 仅仅通过缩减维度或减少层数等手段来降低模型参数量

