import torch
from torch.utils.data import Dataset
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from os import listdir
from os.path import join
from torchvision.transforms import Compose, RandomCrop, ToTensor, ToPILImage, CenterCrop, Resize, InterpolationMode

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])

def calculate_valid_crop_size(crop_size=128, upscale_factor=4):
    return crop_size - (crop_size % upscale_factor)

def train_hr_transform(crop_size=128):
    return Compose([
        RandomCrop(crop_size),
        ToTensor(),
    ])
def train_lr_transform(crop_size=32):
    return Compose([
        RandomCrop(crop_size),
        ToTensor()
    ])