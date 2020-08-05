from fashion_intel.imports import *

class Attributes(Dataset):
    
    def __init__(self, base_dir, name_df, attr_df):
        self.base_dir = base_dir
        self.attr_df = attr_df
        self.name_df = name_df
        
    def __len__(self):
        return len(self.name_df)
    
    def __getitem__(self, idx):
        # Get id
        _id = self.name_df.iloc[idx]['id']
        
        # Get attrubutes
        _attr = literal_eval(self.attr_df.iloc[idx]['attributes'])
        target = [0]*1000
        for i in _attr:
            target[i] = 1

        target = np.array(target).astype(float)
        
        # Get the feature
        path = os.path.join(self.base_dir, str(_id)+'.npz')
        feature = np.load(path)['v']
        
        
        return torch.from_numpy(feature), torch.tensor(target, dtype=torch.float)