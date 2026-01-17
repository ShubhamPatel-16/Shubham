import pandas as pd 

# print(pd.__version__)
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4 , 5, 6],
#     'C': [7, 8, 9]
# })  
# print(df)
# print(type(df))
# # desc = df.describe()
# # print(desc)   
# df_sorted = df.sort_values(by='B', ascending=False)
# print(df_sorted)
# df = pd.read_csv("Nat_Gas.csv")
data = [100,2332,432]
# data = ['a','f','h']
series = pd.Series(data, index = ["A", "B", "C"])
series.loc["A"] = 200
print(series)