import pandas as pd
import numpy as np

arrests_2015 = pd.read_csv("2015_Arrests.csv")
arrests_2016 = pd.read_csv("2016_Arrests.csv")
arrests_2017 = pd.read_csv("2017_Arrests.csv")
arrests_2018 = pd.read_csv("2018Arrests_YTD_0_2.csv")
arrests_2019 = pd.read_csv("2019Arrests_YTD_0_2.csv")
arrests_2020 = pd.read_csv("2020_Arrests_0_3.csv")
arrests_2021 = pd.read_csv("2021Arrests_YTD_0_3.csv")
arrests_2022 = pd.read_csv("2022Arrests_YTD_0_2.csv")
arrests_2023 = pd.read_csv("2023_Arrests_0_1.csv")
arrests_2024 = pd.read_csv("2024Arrests_YTD_0_3.csv")

combined_arrests = pd.concat(
    [
        arrests_2015,
        arrests_2016,
        arrests_2017,
        arrests_2018,
        arrests_2019,
        arrests_2020,
        arrests_2021,
        arrests_2022,
        arrests_2023,
        arrests_2024,
    ]
)

name_id = combined_arrests[["Name_ID"]]
repeats = name_id["Name_ID"].value_counts()
repeats_more_than_1 = repeats[repeats > 1]

# print(
#     f"Reoffenders: {len(repeats_more_than_1)} \n Total: {len(combined_arrests)} \n Percentage: {len(repeats_more_than_1) / len(combined_arrests)}"
# )

combined_arrests["Reoffender"] = np.where(
    combined_arrests["Name_ID"].isin(repeats_more_than_1.index), 1, 0
)

combined_arrests = combined_arrests.drop_duplicates(subset=["Name_ID"])
# print(len(combined_arrests), len(combined_arrests[combined_arrests["Reoffender"] == 1]))

combined_arrests.to_csv("combined_arrests.csv", index=False)
