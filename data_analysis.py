import pandas as pd

combined_arrests = pd.read_csv("combined_arrests.csv")

combined_arrests["race"] = combined_arrests["race"].map(
    {"W": 1, "B": 2, "A": 3, "I": 4, "U": 5}
)
combined_arrests["gender"] = combined_arrests["sex"].map({"M": 1, "F": 0})

numeric_columns = combined_arrests.select_dtypes(include=["int64", "float64"]).columns
print(combined_arrests[numeric_columns].corr())
