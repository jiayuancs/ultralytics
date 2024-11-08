"""
该文件用于debug
训练YOLO模型建议使用命令行工具
"""

import os
import argparse

from ultralytics import YOLO


def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='ChinaMobile9000.yaml', type=str, help="数据集")
    parser.add_argument('--cfg', default='ultralytics/cfg/models/mobile/yolo11n-tiny-mini-v2.yaml', type=str, help="模型结构")
    parser.add_argument('--epochs', default=300, type=int)
    parser.add_argument('--imgsz', default=640, type=int)
    parser.add_argument('--batch', default=32, type=int)
    args = parser.parse_args()
    print(args)
    return args

def training(args):
    datapath = args.data
    if not os.path.exists(datapath):
        datapath = os.path.join(os.path.dirname(__file__), "dataset", os.path.basename(datapath))
    assert os.path.exists(datapath), "dataset yaml file not found"

    model = YOLO(model=args.cfg, task="detect")

    # 参数的含义具体见 https://docs.ultralytics.com/modes/train/#train-settings
    model.train(
        data=datapath,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch
    )


if __name__ == "__main__":
    args = get_opt()
    training(args=args)
