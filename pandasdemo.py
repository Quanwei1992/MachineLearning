import pandas as pd
import numpy as np

print(pd.__version__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
np.log(population)

df = pd.DataFrame({ 'City name': city_names, 'Population': population })

print(df.head())

print(df['City name'][0:1])

