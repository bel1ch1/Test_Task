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
        counter = 0
        for box in boxes:
            counter += 1
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        text = f'Detected: {counter}'
        font = cv2.FONT_ITALIC
        font_scale = 2
        color = (0, 0, 255)
        thickness = 3
        margin = 20

        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

        x_pos = frame.shape[1] - text_width - margin
        y_pos = text_height + margin

        cv2.putText(frame, text, (x_pos, y_pos), font, font_scale, color, thickness, cv2.LINE_AA)

        writer.write(frame)
    writer.release()
