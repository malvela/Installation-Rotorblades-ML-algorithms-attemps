import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from glob import glob
import time
from datetime import datetime
from scipy.stats import pearsonr


# generating dataframe
# from dictionaries
results = sorted(glob('Results_preprocessing/geometry_files/**.csv'))
# return cm
# by iterating through the data frame and putting it into dictionaries?
def getCM(data):
    data = pd.DataFrame.from_dict(data)
    data = data.astype('float')
    corrMatrix = data.corr(method = 'pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.savefig("corrMatrix.png")
    plt.show()
def getCM_df1s(data, label):
    data = data.resample('1S', label='left').sum().pad()
    data = data.astype('float')
    corrMatrix = data.corr(method='pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.title('Correlation Matrix 1s')
    plt.savefig(f'correlationsmatrixes/CorrelationMatrix1s{[i]}.png')
    plt.show()
def getCM_df1m(data, label):
    data = data.resample('1T', label='left').sum().pad()
    data = data.astype('float')
    corrMatrix = data.corr(method='pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.title('Correlation Matrix 1m')
    plt.savefig(f'correlationsmatrixes/CorrelationMatrix1m{[i]}.png')
    plt.show()
def getCM_df10m(data, label):
    data = data.resample('10T', label='left').sum().pad()
    data = data.astype('float')
    corrMatrix = data.corr(method='pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.title('Correlation Matrix 10m')
    plt.savefig(f'correlationsmatrixes/CorrelationMatrix10m{[i]}.png')
    plt.show()
def getCM_df30m(data, label):
    data = data.resample('30T', label='left').sum().pad()
    data = data.astype('float')
    corrMatrix = data.corr(method='pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.title('Correlation Matrix 30m')
    plt.savefig(f'correlationsmatrixes/CorrelationMatrix30m{[i]}.png')
    plt.show()
def getCM_df1h(data, label):
    data = data.resample('1H', label='left').sum().pad()
    data = data.astype('float')
    corrMatrix = data.corr(method='pearson')
    plt.figure(figsize=(10, 10))  # hierkannst du die Plotgröße verändern
    sn.heatmap(corrMatrix, annot=True)
    plt.legend()
    plt.title('Correlation Matrix 1h')
    plt.savefig(f'correlationsmatrixes/CorrelationMatrix1h{[i]}.png')
    plt.show()



#getCM(data) #testing CorrelationMatrix
'''
#einlesen der Daten:
data = pd.read_csv('hammerhead_reduced.csv', delimiter = ',')
UTC = []
for i in range(len(data)):
    UTC.append(datetime.strptime(data.iloc[i,0], '%Y-%m-%d %H:%M:%S'))
data.index = UTC
data = data.resample('1T', label='left').sum().pad()
data_1 =  data.resample('1T', label='left').sum().pad()
data_10 =  data.resample('10T', label='left').sum().pad()
data_30 =  data.resample('30T', label='left').sum().pad()
data_1h =  data.resample('1H', label='left').sum().pad()

getCM_df(data)
getCM_df(data_1)
getCM_df(data_10)
getCM_df(data_30)
getCM_df(data_1h)
'''

for i in range(len(results)):
    data = pd.read_csv(results[i], delimiter=',')
    label = results[i]
    UTC = []
    for j in range(len(data)):
        UTC.append(datetime.strptime(data.iloc[j , 0], '%Y-%m-%d %H:%M:%S'))
    data.index = UTC
    del data['epoch']
    plt.plot(0,0,label= label)
    plt.legend()
    plt.show()
    getCM_df1m(data, i)
    getCM_df1s(data, i)
    getCM_df10m(data, i)
    getCM_df30m(data, i)
    getCM_df1h(data, i)

'''
data = pd.read_csv(results[0], delimiter=',')
UTC = []
for i in range(len(data)):
    UTC.append(datetime.strptime(data.iloc[i,0], '%Y-%m-%d %H:%M:%S'))
data.index = UTC
del data['epoch']
data = data.astype('float')
corrMatrix = data.corr(method='pearson')
result = []
for i in range(11):
    for j in range(11):
        datei = open(f'correlationresult.txt', 'a')
        if abs(corrMatrix.iloc[i, j]) > 0.5:
            datei.write(f"{corrMatrix.iloc[i,j]} fuer Korrelation zwischen {corrMatrix.columns[i]} und {corrMatrix.index[j]}\n ")
        datei.close()
'''


