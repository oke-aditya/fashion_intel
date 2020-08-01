import pandas as pd

df = pd.read_fwf("data/labels.txt")
df.to_csv("labels.csv")
