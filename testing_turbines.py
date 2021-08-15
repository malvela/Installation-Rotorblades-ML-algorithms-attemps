import pandas as pd
import numpy as np
from glob import glob

results = sorted(glob('Results_preprocessing/turbine04/**.csv'))
for name in results:
    print(name)
    data = pd.read_csv(name, delimiter = ',')
    print(data.columns)
    print(data.iloc[0,0])
    print(data.iloc[-1,0])
