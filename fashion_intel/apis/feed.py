from fashion_intel.imports import *

__all__ = ["Feed"]


class Feed:
    """
    This class contains functions to support the fashion feed
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df

    def get_feed(self, category: int, order: int, limit: int) -> List:
        """ This function is used to get images for feed
        Args:
            category: class label of product category
            order: 0 for trending 1 for lagging
            limit: number of image ids to return
        
        Return:
            List: list of image ids
        """

        if order == 0:
            indices = self.df.nlargest(limit, "score").index
        else:
            indices = self.df.nsmallest(limit, "score").index

        result = [df.iloc[idx]["id"] for idx in indices]

        return result


if __name__ == "__main__":

    df_path = "./data/tables/scores.csv"
    df = pd.read_csv(df_path)

    feed = Feed(df)

    result = feed.get_feed(0, 0, 20)

    print(result)
