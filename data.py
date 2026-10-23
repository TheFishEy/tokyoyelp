import pandas as pd

df = pd.read_csv("restaurants.csv")

print("Rows and columns:", df.shape)
print("Column names:", df.columns.tolist())
print(df.head(3).to_string())