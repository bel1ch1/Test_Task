from ultralytics import YOLO
import cv2


class PeopleDetector:
    '''СLass for detecting people using YOLO model.

    Args:
        model_path (str): (Optional) Path to the model file.
        conf_threshold (float): (Optional) Confidence threshold for detection.
    '''
    def __init__(self, model_path='yolo11n.pt', conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.class_id = 0 # person class in the COCO training dataset
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        '''Finds the people in the frame and returns the bounding boxes.

        Args:
            frame (np.ndarray): Input frame in BGR format.

        Return:
            list: List of bounding boxes in the format [x1, y1, x2, y2].
        '''
        results = self.model(frame)
        boxes = []
        for result in results:
            for box in result.boxes:
                if int(box.cls) == self.class_id and box.conf >= self.conf_threshold:
                    boxes.append(box.xyxy[0].tolist())
        return boxes
