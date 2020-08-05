from fashion_intel.imports import *

class Siamese(pl.LightningModule):
    
    def __init__(self, in_features=512):
        
        super().__init__()
        self.fc1 = nn.Linear(in_features=512, out_features=512)
        self.relu = nn.ReLU()
        self.criterion = nn.TripletMarginLoss(margin=1.0, p=2)
    
    def forward(self, image):
        image_emb = self.relu(self.fc1(image))
        return image_emb
    
    def training_step(self, batch, batch_idx):
        anchor, pos, neg = batch
        anchor_emb = self(anchor)
        pos_emb = self(pos)
        neg_emb = self(neg)
        loss = self.criterion(anchor_emb, pos_emb, neg_emb)
        
        return {'loss':loss,'log':{'train_loss':loss}}
    
    def validation_step(self, batch, batch_idx):
        anchor, pos, neg = batch
        anchor_emb = self(anchor)
        pos_emb = self(pos)
        neg_emb = self(neg)
        loss = self.criterion(anchor_emb, pos_emb, neg_emb)
        
        return {'val_loss':loss, 'log':{'val_loss':loss}}
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.00006)