#!/bin/bash
# 各参数的含义具体见 https://docs.ultralytics.com/modes/train/#train-settings
yolo detect train \
data=dataset/ChinaMobile9000.yaml \
model=ultralytics/cfg/models/mobile/yolo11n-tiny-mini.yaml \
epochs=300 \
imgsz=640 \
batch=32 \
name=yolo11n-tiny-mini

# optimizer=AdamW \
# lr0=0.001 \
# lrf=0.001


# tensorboard --host 0.0.0.0 --port 8000  --logdir runs/detect/train17
