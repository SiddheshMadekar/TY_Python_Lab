import pandas as pd

df = pd.read_csv("marks.csv")

series = pd.Series(df["Marks"])

print("Pandas Series:")
print(series)