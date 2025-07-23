import torch
import cv2
from transformers import AutoImageProcessor, AutoModelForImageClassification

print("Torch version:", torch.__version__)
print("OpenCV version:", cv2.__version__)