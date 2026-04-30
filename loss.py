import torch
from torch import nn
import torchvision.models as models
class GeneratorLoss(nn.Module):
    def __init__(self):
        super(GeneratorLoss, self).__init__()
        vgg = models.vgg19(True)
        loss_network = nn.Sequential(*list(vgg.features)).eval()
        for param in loss_network.parameters():
            param.requires_grad = False
        self.loss_network = loss_network
        self.mae_loss = nn.L1Loss()

    def forward(self, out_labels, out_images, target_images):
        # Adversarial Loss
        adversarial_loss = torch.mean(1 - out_labels)
        # Perception Loss
        perception_loss = self.mae_loss(self.loss_network(out_images), self.loss_network(target_images))
        # Image Loss
        image_loss = self.mae_loss(out_images, target_images)
        return image_loss + 0.001 * adversarial_loss + 0.006 * perception_loss

if __name__ == "__main__":
    g_loss = GeneratorLoss()
    print(g_loss)

