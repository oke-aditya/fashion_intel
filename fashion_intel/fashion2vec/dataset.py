from fashion_intel.imports import *


class FashionTriplet(Dataset):
    def __init__(self, df, triplet, root_dir):
        self.df = df
        self.map = df[["id", "class_code"]]
        self.n_class = df["class_code"].nunique()
        self.root_dir = root_dir
        self.triplet = triplet

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        anchor = self.map.iloc[idx]["id"]
        anchor_class = self.map.iloc[idx]["class_code"]

        # Sample positive image
        # pos_id = self.map[self.map['class_code'] == anchor_class].sample(n=1).iloc[0]['id']
        pos_id = self.triplet.iloc[idx]["pos"]
        # Sample negative image
        # neg_id = self.map[self.map['class_code'] != anchor_class].sample(n=1).iloc[0]['id']
        neg_id = self.triplet.iloc[idx]["negs"]

        pos_feature = np.load(os.path.join(self.root_dir, str(pos_id) + ".npz"))["v"]
        neg_feature = np.load(os.path.join(self.root_dir, str(neg_id) + ".npz"))["v"]
        anchor_feature = np.load(os.path.join(self.root_dir, str(anchor) + ".npz"))["v"]

        return (
            torch.tensor(anchor_feature),
            torch.tensor(pos_feature),
            torch.tensor(neg_feature),
        )
