import os
import numpy as np
import cv2
from PIL import Image
import torch
from torch.utils.data import DataLoader, Dataset


class detection_dataset(Dataset):
    def __init__(self, dataframe, target, transforms=None, train=True):
        super().__init__()

        self.image_ids = dataframe["image_id"].unique()
        self.transforms = transforms
        self.df = dataframe
        self.train = train
        self.target = target

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        img_path = self.image_ids[index]
        xtl = self.df["xtl"][index]
        xbr = self.df["xbr"][index]
        ytl = self.df["ytl"][index]
        ybr = self.df["ybr"][index]
        label = self.df[self.target][index]

        image = Image.open(img_path)
        if self.transforms is not None:  # Apply transformation
            image = self.transforms(image)

        boxes = [[xtl, ytl, xbr, ybr]]
        boxes = torch.as_tensor(boxes, dtype=torch.float32)

        area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
        area = torch.as_tensor(area, dtype=torch.float32)

        # For has_mask
        labels = torch.as_tensor([label], dtype=torch.int64)
        # print(labels)

        target = {}
        target["boxes"] = boxes
        target["labels"] = labels
        target["image_id"] = torch.tensor([index])
        target["area"] = area

        return image, target
