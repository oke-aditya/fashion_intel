from fashion_intel.imports import *

__all__ = ["Ranker", "BayesianRanker"]


class Ranker:
    def __init__(self, ids, features_dir):
        self.ids = ids
        self.features_dir = features_dir

    def load_features(self):

        _list = []
        for _id in tqdm(self.ids):
            _file = str(_id) + ".npz"
            _path = os.path.join(self.features_dir, _file)
            feat = np.load(_path)
            _list.append(feat["v"])

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
        self.score = sorted(
            ((pagerank_score[i], s) for i, s in enumerate(self.ids)), reverse=True
        )

    def normalize_score(self):

        scaler = MinMaxScaler()
        _scores = [[_score[0]] for _score in self.score]
        normalized_score = scaler.fit_transform(_scores)

        self.score = [
            [normalized_score[idx][0], _tup[1]] for idx, _tup in enumerate(self.score)
        ]

        return self.score


class BayesianRanker:
    """
    This class ranks fashion from e-commerce sites using ratings
    """

    def __init__(self, df, scale):
        self.df = df
        self.scale = scale

    def load_variables(self):
        self.mean_rating = self.df["rating"].mean()
        self.min_review = self.df["reviews  "].min()

    def true_rating(self, rating, review, scale):
        t_rating = (self.mean_rating * self.min_reviews + rating * reviews) / (
            self.min_reviews + reviews
        )
        t_rating = t_rating / self.scale
        return t_rating

    def rank_products(self):
        self.df["true_rating"] = self.df.apply(
            lambda row: self.true_rating(row["rating"], row["reviews"], self.scale),
            axis=1,
        )
        return self.df


if __name__ == "__main__":

    df_path = "./data/tables/smol.csv"
    df = pd.read_csv(df_path)

    print("[INFO] Loaded dataframe")

    _ids = df["id"].tolist()

    # Sample 1k ids
    _ids = _ids[:100]

    # Test model
    features_dir = "./data/features"
    ranker = Ranker(_ids, features_dir)

    ranker.load_features()
    ranker.build_matrix()
    ranker.build_graph()

    ranker.compute_score()

    scores = ranker.normalize_score()

    # _indices = [_score[1] for _score in scores]
    # _scores = [_score[0] for _score in scores]

    # df = pd.DataFrame({'id':_indices,'score':_scores})
    # df.to_csv('./data/tables/scores.csv', index=None)

    # Bayesian ranker test
    amazon_df_path = "./data/tables/amazon-tshirt.csv"

    b_df = pd.read_csv(amazon_df_path)

    bayesian_ranker = BayesianRanker(b_df, scale=5)

    bayesian_ranker.load_variables()
    modified_df = bayesian_ranker.rank_products()

    print(modified_df.head())
