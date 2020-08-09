# This script does only inference from the loaded model
import cv2

# import matplotlib.pyplot as plt
import torch
import model
import os
from PIL import Image
import torchvision.transforms as T
import config

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")


def load_model():
    detector = model.create_model(num_classes=config.NUM_CLASSES)
    # print(detector)
    detector.load_state_dict(torch.load(config.MODEL_SAVE_PATH, map_location=device))
    # print(detector)
    detector.eval()
    detector.to(device)
    return detector


# Load the detector for inference
def load_image_tensor(image_path, device):
    image_tensor = T.ToTensor()(Image.open(image_path))
    input_images = [image_tensor.to(device)]
    return input_images


def get_prediction(detector, image_path):
    # We can do a batch prediction as well but right now I'm doing on single image
    # Batch prediction can improve time but let's keep it simple for now.
    input_images = load_image_tensor(image_path, device)
    prediction_d = {}
    with torch.no_grad():
        prediction = detector(input_images)
        # for pred in prediction:
        #     boxes = pred["boxes"].data.cpu().numpy()
        #     labels = pred["labels"].data.cpu().numpy()
        #     scores = pred["scores"].data.cpu().numpy()

    return prediction


if __name__ == "__main__":
    pass
