import pandas as pd

# df = pd.read_csv("labels.csv")
# df = pd.read_csv("cleaned_labels.csv")
# print(df.head())

# print(df.columns)

# df = pd.read_csv("final_data.csv")

# df.to_csv("final_data2.csv", index=False)

# df = df.drop(["Unnamed: 0", "id"], axis=1)
# df.to_csv("cleaned_labels3.csv", index=False)

# df = df.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], axis=1)
# df.to_csv("cleaned_labels1.csv")

# for i in range(len(df)):
#     img_name = str(df['image_path'][i])
#     img_l = img_name.split('/')
#     img_name1 = str(img_l[1:3][0])
#     img_name2 = str(img_l[1:3][1])

#     target_name = img_name1 + "_" + img_name2
#     df['target'][i] = target_name
#     all_targets.add(target_name)

#     # print(img_name1)
#     # print(img_name2)

# cnt = 1
# map_dict = {}
# for i in all_targets_list:
#     map_dict[i] = cnt
#     cnt += 1

# for i in range(len(df)):
#     df['final_target'][i] = map_dict[df['target'][i]]
