import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({"Day 1": [7,1,5,6,3,10,5,8],
                    "Day 2" : [1,2,8,4,3,9,5,2]})

sns.lineplot(data = df)
plt.savefig('filename.png')



#6. Plotten Sie die Funktion f (x) = x2 f ̈ur Werte von x von -10 bis +10. (Datei
#plot x power 2.png)
#7. Plotten Sie die Funktion g(x) = x3 f ̈ur Werte von x von -10 bis +10. (Datei
#plot x power 3.png)
#8. Plotten Sie beide Funktionen f in blau und g in rot in denselben Graphen. (Datei
#plot x power 2 and 3.png)

