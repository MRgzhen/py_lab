# yolo_lab

YOLO 目标检测学习实验。使用 ultralytics 训练模型，labelImg 标注数据。

## 环境搭建

### 1. 用 conda 创建虚拟环境

```bash
conda create -n yolo_lab python=3.10
```

### 2. 切换到虚拟环境

```bash
conda activate yolo_lab
```

### 3. 用 pip 安装依赖

```bash
pip install torch torchvision torchaudio jupyterlab ultralytics==8.3.55
```

### 4. 安装标注工具 labelImg

```bash
pip install labelImg
```

## 运行

启动 JupyterLab：

```bash
jupyter lab
```

启动标注工具：

```bash
labelImg
```
