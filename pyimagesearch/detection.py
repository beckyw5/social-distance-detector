# import the necessary packages
from .social_distancing_config import NMS_THRESH
from .social_distancing_config import MIN_CONF

import numpy as np
import cv2


def detect_people(frame, net, ln, personIdx=0):
    # frame - from video file
    # net - pre-initialized and pre-trained YOLO object detection model
    # ln - YOLO CNN output layer names
    # personIdx - getting the object at index position 0 from object file (person)

    (H, W) = frame.shape[:2]
    # grab the dimensions of the frame and  initialize the list of
    results = []
    # results
