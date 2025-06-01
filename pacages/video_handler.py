import cv2


class VideoHandler:
    '''A class for reading and writing video files.

    Args:
        video_path (str): Path to the output video file.
    '''
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_frames(self):
        '''Frame Generator.

        Yilds:
            np.ndarray: One frame of the video in BGR format.
        '''
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame
        self.cap.release()

    def create_writer(self, output_path):
        '''Creates a VideoWriter object to save the result.

        Args:
            output_path (str): The path to save the output video.

        Returns:
            cv2.VideoWriter: An object for recording video.
        '''
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        return cv2.VideoWriter(
            output_path, fourcc, self.fps, (self.width, self.height)
        )
