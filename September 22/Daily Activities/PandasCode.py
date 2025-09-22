import numpy as np
import pandas as pd

data = {
    "name": ["john","johnny","dilip"],
    "age" : [22,23,55],
    "course" : ["ai","ml","dl"]
}

df = pd.DataFrame(data)
print(df)
# print(df["name"])#one column accessing
# print(df[["name","age"]])#multiple column accessing
# print(df.iloc[0])#for row vise fetching the data
# print(df.loc[2, "age"])#for column vise fetching the data
#
# #filtering data
# old_age = df[df["age"] > 30]
# print(old_age)

#adding and updating the columns
df["Result"] = np.where(df["age"] > 30,"old","young")
df.loc[df["name"] == "john" , "course"] == "ccvt"
print(df["Result"])
