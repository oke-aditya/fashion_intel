from fashion_intel.imports import *


__all__ = ["Tagger"]


class Tagger(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.fc0 = nn.Linear(in_features=512, out_features=1000)
        self.criterion = nn.BCELoss()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(self.fc0(x))

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.criterion(y_hat, y)

        return {"loss": loss, "log": {"train_loss": loss}}

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.criterion(y_hat, y)
        return {"val_loss": loss, "log": {"val_loss": loss}}

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.0005)
