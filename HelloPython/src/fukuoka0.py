import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("fukuoka0.csv", skiprows=[0,1,2,4,5], index_col=0 )
df = df.drop(df.columns[[1,2]],axis=1)
print(df.head())
print(df.tail())
df.index = pd.to_datetime(df.index)
df.plot(title='Fukuoka(2019)')
plt.show()



