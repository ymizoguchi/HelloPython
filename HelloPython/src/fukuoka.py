import pandas as pd
import matplotlib
font = {'family': 'IPAexGothic'}
matplotlib.rc('font', **font)
df = pd.read_csv("fukuoka.csv", skiprows=[0,1,2,4,5], 
                 encoding='shift_jis', index_col=0 )
df = df.drop(df.columns[[1,2]],axis=1)
print(df.head())
print(df.tail())
df.index = pd.to_datetime(df.index)
df.plot(title='福岡市の気温(2019年)')
matplotlib.pyplot.show()



