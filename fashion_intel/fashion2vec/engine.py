from fashion_intel.imports import *


class FashionData(Dataset):

  def __init__(self, df_index, root, transform):
    self.df_index = df_index
    self.root = root
    self.transform = transform
  
  def __len__(self):
    return len(self.df_index)
  
  def __getitem__(self, idx):
    _name = self.df_index.iloc[idx][0]
    _id = self.df_index.iloc[idx][1]
    path = os.path.join(self.root, _name)
    image = Image.open(path)
    if transform:
      image = self.transform(image)
    return _id, image


class Fashion2VecEngine:
    """ This class generates embeddings 
    """

    def __init__(self):
        pass

    def load_data(self):
        transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        root = '/content/img'
        data = FashionData(df_index, root, transform)   

        loader = DataLoader(data, batch_size=64, num_workers=2)

    
    def generate_embeddings(self):
        path = '/content/features'
        for batch in tqdm(loader):
        ids, images = batch
        bs,_,_,_ = images.shape
        features = resnet(images.cuda())
        features = features.reshape(bs,-1)
        features = features.cpu().detach().numpy()

        ids = ids.tolist()
        for i in range(bs):
            loc = os.path.join(path, str(ids[i])+'.npz')
            #joblib.dump(features[i], loc)
            np.savez_compressed(loc, v=features[i])