""" Launch file """

import argparse
from pacages.model_processing import model_processing

def arg_parser():
    '''Parse command line arguments.

    Returns:
        argparse.Namespace: An object with arguments:
            - input (str): The path to the input video.
            - output (str): The path to save the result.
            - conf (float): Confidence threshold (0-1).
    '''
    parser = argparse.ArgumentParser(description='The detector of people in the video')
    parser.add_argument('--input', required=True, help='Input video file')
    parser.add_argument('--output', required=True, help='Output video file')
    parser.add_argument('--conf', type=float, default=0.5,
                       help='Confidence threshold (0-1)')
    return parser.parse_args()

if __name__ == '__main__':
    args = arg_parser()
    model_processing(args.input, args.output, args.conf)
