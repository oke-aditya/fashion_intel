from fashion_intel.imports import *

class Ranker:
    def __init__(self, ids, features_dir):
        self.ids = ids
        self.features_dir = features_dir
        
    def load_features(self):
        
        _list = []
        for _id in tqdm(self.ids):
            _file = _id+'.npz'
            _path = os.path.join(self.features_dir, _file)
            feat = np.load(_path)
            _list.append(feat['v'])
            
        self.A = np.array(_list)
        
    def build_matrix(self):
        
        similarity = np.dot(self.A, self.A.T)

        square_mag = np.diag(similarity)

        inv_square_mag = 1 / square_mag

        inv_square_mag[np.isinf(inv_square_mag)] = 0

        inv_mag = np.sqrt(inv_square_mag)

        cosine = similarity * inv_mag
        cosine = cosine.T * inv_mag
        self.cosine = cosine
        
    def build_graph(self):
        sim_graph = nx.from_numpy_array(self.cosine)
        self.sim_graph = sim_graph
        
    def compute_score(self):
        pagerank_score = nx.pagerank(self.sim_graph)
        self.score = sorted(((pagerank_score[i], s) for i,s in enumerate(self.ids)), reverse=True)
        return self.score
    def normalize_score(self):
        pass