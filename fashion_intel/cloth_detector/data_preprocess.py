import pandas as pd

# df = pd.read_csv("labels.csv")
df = pd.read_csv("cleaned_labels.csv")
print(df.head())

print(df.columns)

# df = df.drop(["Unnamed: 0", "id"], axis=1)
# df.to_csv("cleaned_labels3.csv", index=False)

# df = df.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], axis=1)
# df.to_csv("cleaned_labels1.csv")
