import numpy as np
import pandas as pd
import pickle
import keras
from numpy import array

import matplotlib.pyplot as plt

def predict_ROLF(data):
    with open('rolf.pickle', 'rb') as handle:
        rolf = pickle.load(handle)
    #preproccessed data
    data = pd.DataFrame.from_dict(data)
    del data['epoch']
    data = data.to_numpy()
    data = data.astype('float64')
    results = []
    for i in range(len(data)):
        results.append(rolf.predict(data[i]))
    return results

def predict_NN(data):
    model = keras.models.load_model('model.h5')
    data = pd.DataFrame.from_dict(data)
    del data['epoch']
    data = data.to_numpy()
    data = data.astype('float64')
    results = []
    for i in range(len(data)):
        results.append(np.argmax(model.predict(array([data[i]])))-1)
    return results
def predict(data):
    result1 = predict_ROLF(data)
    result2 = predict_NN(data)
    result1 = np.array(result1)
    result2 = np.array(result2)

    assert len(result1) == len(result2)
    # result = pd.concat([result1, result1],axis = 1)
    counter1 = np.zeros(29)
    counter2 = np.zeros(29)
    for int in np.unique(result1):
        for i in range(len(result1)):
            if result1[i] == int:
                counter1[int] = counter1[int] + 1
    for int in np.unique(result2):
        for i in range(len(result2)):
            if result1[i] == int:
                counter2[int] = counter2[int] + 1
    colors1 = []
    for i in range(29):
        color = list(np.random.choice(range(256), size=3) / 256)
        colors1.append(color)
    colors2 = []
    for i in range(29):
        color = list(np.random.choice(range(256), size=3) / 256)
        colors2.append(color)

    plt.bar(x=np.arange(29), height=counter1, color=colors1)
    plt.bar(x=np.arange(29), height=counter2, color=colors2)
    plt.title('occurance of predicted clusters')
    plt.xlabel('cluster/class')
    plt.xticks(np.arange(29), rotation=90)
    plt.ylabel('occurance')
    plt.savefig('prediction.png')
    plt.show()
