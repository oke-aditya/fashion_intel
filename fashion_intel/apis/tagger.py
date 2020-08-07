from fashion_intel.imports import *
from fashion_intel.tagger import *

__all__ = ["FashionTagger"]


class FashionTagger:
    """ 
    A class to provide image tagging 
    """

    def __init__(self, state_dict, vec_dir, map_dir):

        self.tagger = Tagger()
        self.tagger.eval()
        self.tagger.load_state_dict(state_dict)

        self.vec_dir = vec_dir

        self.map_dir = map_dir

        # Loading rev maps

        with open(os.path.join(self.map_dir, "attr_labels.pkl"), "rb") as f:
            self.attr_labels = pickle.load(f)
        with open(os.path.join(self.map_dir, "attr_types.pkl"), "rb") as f:
            self.attr_types = pickle.load(f)
        with open(os.path.join(self.map_dir, "attr_to_type.pkl"), "rb") as f:
            self.attr_to_type = pickle.load(f)

    def get_tags(self, image_id: int) -> str:
        """ This function is used to get images for feed
        Args:
            image_id: id of image
        Return:
            str: the generated description of image
        """

        feat_path = os.path.join(self.vec_dir, str(image_id) + ".npz")
        feature = np.load(feat_path)["v"]
        _in = torch.from_numpy(feature)

        _out = self.tagger(_in)
        _out = _out.data.numpy()

        indices = _out.argsort()[-4:][::-1].tolist()

        tag = self.indx2tag(indices)

        return tag

    def indx2tag(self, indices):

        attrs = [self.attr_labels[idx] for idx in indices]

        meta = dict()

        for attr in attrs:
            key = self.attr_to_type[attr]
            if key in meta:
                meta[key].append(attr)
            else:
                meta[key] = [attr]

        tag = ""
        for _type in meta:
            _type_tag = self.attr_types[_type]
            _attrs = " ".join(meta[_type])
            tag += _type_tag + ": " + _attrs + "\n"

        return tag


if __name__ == "__main__":

    state_path = "./models/tagger.pt"
    state_dict = torch.load(state_path)

    vec_dir = "./data/features"
    util_dir = "./data/utils"

    fashion_tagger = FashionTagger(state_dict, vec_dir, util_dir)

    _tag = fashion_tagger.get_tags(10)

    print(_tag)
