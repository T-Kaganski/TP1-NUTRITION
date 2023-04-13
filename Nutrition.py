import pandas as pd
import numpy as np


data = pd.read_csv('nutrition.csv', sep=";")
df = pd.DataFrame(data)
#print(df.to_markdown())

#df2 = df[['Id', 'Catégorie', 'Description']]
df2 = df.sort_values(by='Id', ascending=True)
df2 = df2[df2["Id"] == 59]
print(df2.to_markdown())