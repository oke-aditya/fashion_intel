from fashion_intel.imports import *
import config

__all__ = ["FAISS"]


class FAISS:
    """
    This class contains functions related to product reccomendation
    """

    def __init__(self, ids, vec_dir):
        self.ids = ids
        self.vec_dir = vec_dir

    def load_vectors(self):

        _list = []
        for _id in tqdm(self.ids):
            _file = str(_id) + ".npz"
            _path = os.path.join(self.vec_dir, _file)
            feat = np.load(_path)
            _list.append(feat["v"])

        self.features = np.array(_list)

        # Vector dimensions
        self.dim = 512

        np.random.seed(13)
        self.db_vectors = np.asarray(self.features, dtype=np.float32)

    def build_index(self):

        self.index = faiss.IndexFlatL2(self.dim)
        self.index.add(self.db_vectors)

    def get_similar(self, id: int, limit: int) -> List:
        """ This function is used to get similar images
        Args:
            id: the id of image
            limit: number of similar image ids to return
        
        Return:
            List: list of similar image ids
        """

        xq_path = os.path.join(self.vec_dir, str(id) + ".npz")
        xq = np.load(xq_path)["v"]

        query = np.transpose(xq.reshape(self.dim, 1))

        D, I = self.index.search(query, limit)

        return D, I


if __name__ == "__main__":
    df_path = "./data/tables/smol.csv"
    df = pd.read_csv(df_path)

    print("[INFO] Loaded dataframe")

    _ids = df["id"].tolist()

    # Sample 1k ids
    _ids = _ids[:100]

    # Test model
    features_dir = config.features_dir
    engine = FAISS(_ids, features_dir)

    engine.load_vectors()

    engine.build_index()

    # Top 5 similar
    D, I = engine.get_similar(1, 5)
