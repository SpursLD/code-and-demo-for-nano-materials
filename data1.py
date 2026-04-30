from torch.utils.data import Dataset
from PIL import Image
import os
from torchvision.transforms import Compose, RandomCrop, ToTensor, ToPILImage, CenterCrop, Resize, InterpolationMode
import torchvision.transforms as transforms
class PreprocessDatset(Dataset):
    def __init__(self, hr_path, lr_path):
        self.hr_path = hr_path
        self.lr_path = lr_path
        self.hr_img_path = os.listdir(self.hr_path)
        self.lr_img_path = os.listdir(self.lr_path)
    def __getitem__(self, idx):
        lr_img_name = self.lr_img_path[idx]
        lr_img_item_path = os.path.join(self.lr_path, lr_img_name)
        lr_img = transforms.ToTensor()(Image.open(lr_img_item_path))
        hr_img_name = self.hr_img_path[idx]
        hr_img_item_path = os.path.join(self.hr_path, hr_img_name)
        hr_img = transforms.ToTensor()(Image.open(hr_img_item_path))
        return lr_img, hr_img
    def __len__(self):
        return len(self.lr_img_path)

def display_transform():
    return Compose([
        ToPILImage(),
        Resize(400),
        CenterCrop(400),
        ToTensor()
    ])

