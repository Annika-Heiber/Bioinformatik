import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({"Day 1": [7,1,5,6,3,10,5,8],
                    "Day 2" : [1,2,8,4,3,9,5,2]})

sns.lineplot(data = df)
plt.savefig('filename.png')
