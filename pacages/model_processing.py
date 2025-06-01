import cv2
from .detector import PeopleDetector
from .video_handler import VideoHandler

def model_processing(input_path, output_path, conf_threshold=0.5):
    '''Processes videos using modules.

    Args:
        input_path (str): The path to the input video.
        output_path (str): The path to save the result.
        conf_threshold (float): (Optional) Confidence threshold for detection.
    '''
    detector = PeopleDetector(conf_threshold=conf_threshold)
    video = VideoHandler(input_path)
    writer = video.create_writer(output_path)

    for frame in video.get_frames():
        boxes = detector.detect(frame)
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        writer.write(frame)
    writer.release()
