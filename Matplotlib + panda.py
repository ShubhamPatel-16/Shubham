import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
type_count = df['Type1'].value_counts()

plt.barh(type_count.index, type_count.values, color = 'lightgreen', edgecolor = 'black')

plt.title('Count of Pokemon by Type')
plt.xlabel('Count')
plt.ylabel('Pokemon Type')

plt.tight_layout()
plt.show()