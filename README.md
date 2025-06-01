# People Detection in Video using YOLOv11

![OpenCV](https://img.shields.io/badge/OpenCV-5.0-blue)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv11-red)
![Python](https://img.shields.io/badge/Python-3.11-green)

A computer vision pipeline for detecting people in video files using YOLOv11n model. The project features modular architecture, configurable confidence threshold, and produces annotated output videos.

## Features

- **YOLOv11-based detection** - Uses efficient YOLOv11n model pretrained on COCO dataset
- **Video processing** - Handles input/output video files with preserved metadata
- **Configurable confidence** - Adjust detection sensitivity via command line
- **Modular design** - Separated model, video handling, and processing logic
- **Visualization** - Draws bounding boxes around detected people

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bel1ch1/test_task.git
cd people-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python ultralytics
```

## Usage

Basic command:
```bash
python main.py --input crowd.mp4 --output output.mp4 --conf 0.5
```

Arguments:
| Argument    | Description                     | Default | Required |
|:-----------:|:------------------------------:|:-------:|:--------:|
| `--input`   | Path to input video file        | -       | Yes      |
| `--output`  | Path for annotated output video | -       | Yes      |
| `--conf`    | Confidence threshold (0.0-1.0)  | 0.5     | No       |
