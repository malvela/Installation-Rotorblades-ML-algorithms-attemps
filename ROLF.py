#%%

import matplotlib.pyplot as plt

from sklearn import datasets
import time
import numpy as np
import pandas as pd
import seaborn as sn
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
#%%

from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pickle as pickle

class ROLF():
    def __init__(self,p=1.5,lr_center = 0.1, lr_sigma = 0.1,initSigma = 2,strategy = ''):
        self.p = p
        self.lr_center = lr_center
        self.lr_sigma = lr_sigma
        self.initSigma = initSigma
        self.lables = None
        self.assignmensts = None
        self.center = None
        self.sigma = None
        self.strategy = strategy

    def _setSigma_Standard(self):
        return self.initSigma
    def _setSigma_Minimum(self):
        return np.min(self.sigma)
    def _setSigma_Maximum(self):
        return np.max(self.sigma)
    def _setSigma_Mean(self):
        return np.mean(self.sigma)

    def _set_setSigma_Strategy(self,strategy):
        """set the choosen strategy to init new neurons sigma"""
        if strategy == "min":
            return self._setSigma_Minimum
        elif strategy == "max":
            return self._setSigma_Maximum
        elif strategy == "mean":
            return self._setSigma_Mean
        else:
            return self._setSigma_Standard

    def _find_neurons(self,X,strategy):
        """Find the neurons in out training data
            k is the number of neurons found so far. We use this, so we are able to slice the center
            array, such that we do not have to perform the distance calculation for the zero (non center) elements.
            the first neuron gets initilized on the first pattern right away
        """
        X = np.asarray(X)
        funct_setSigma = self._set_setSigma_Strategy(self.strategy)
        self.center = np.zeros(X.shape)
        self.sigma = np.ones(len(X))*self.initSigma
        self.center[0] = X[0]
        k = 1
        for x in X:
            distance = np.linalg.norm(self.center[:k] - x,axis=1)
            acceptors = np.where(distance <= self.sigma[:k]*self.p)[0]
            if len(acceptors) > 0:
                winner = acceptors[np.argmin(distance[acceptors])]
                self.center[winner] += self.lr_center * (x-self.center[winner])
                self.sigma[winner] += self.lr_sigma * (distance[winner]-self.sigma[winner])
            else:
                self.center[k] = x
                self.sigma[k] = funct_setSigma()
                k += 1
        self.center = self.center[:k]
        self.sigma = self.sigma[:k]

    def _find_neighbourhood(self):
        """calculate the neighbourhood graph and assign cluster labels"""
        cluster_id = 0
        notIterated = list(np.arange(0,len(self.center)))
        self.lables = np.zeros(len(self.center),dtype=int)
        while len(notIterated) > 0:
            stack = [notIterated[0]]
            notIterated.remove(notIterated[0])
            while len(stack) > 0:
                NeuronNeuronDist = np.linalg.norm(self.center[stack[-1]] - self.center[notIterated],axis = 1)
                inPercField = NeuronNeuronDist - ((self.sigma[notIterated] + self.sigma[stack[-1]]) * self.p)
                connected = np.where(inPercField <= 0)
                self.lables[stack[-1]] = cluster_id
                stack.pop()
                for k in np.flip(connected[0]):
                    stack.append(notIterated[k])
                    notIterated.remove(notIterated[k])
            cluster_id += 1

    def fit(self,X,strategy = ""):
        """run the fitting process"""
        self._find_neurons(X,strategy)
        self._find_neighbourhood()

    def predict(self,x):
        """predict the label of a new pattern"""
        distance = np.linalg.norm(self.center - x,axis=1)
        acceptors = np.where(distance <= self.sigma*self.p)[0]
        if len(acceptors) > 0:
            return self.lables[acceptors[0]]
        else:
            return -1
    def savemodel(self):
        np.savetxt('ROLFcenter.csv', self.center, delimiter=',')
        np.savetxt('ROLFlables.csv', self.lables, delimiter=',')

        '''
        df = pd.DataFrame()
        df['labels'] = self.lables
        df['centers0'] = self.center[0]
        df['p'] = self.p
        df['lr_center'] = self.lr_center
        df['lr_sigma'] = self.lr_sigma
        df['initSigma'] = self.initSigma
        print(df.head(5))
        '''
#%%

# Run the examples on your own, replace make_circles with make_moons to change the example
# If you get to much cluster or to less, play around with the initSigma
'''
X = pd.read_csv('hammerhead_reduced.csv', delimiter = ',')
X = X.fillna(0)
del X['epoch']
#Z,y = datasets.make_moons(n_samples=100000, noise=0.05)
rolf = ROLF(p=2,lr_center = 0.01, lr_sigma = 0.01,initSigma = 20, strategy = 'max')
start_time = time.time()
rolf.fit(X)
with open('rolf.pickle', 'wb') as handle:
    pickle.dump(rolf, handle)
    handle.close()
print('')
print("fitting ROLF took %s seconds" % (time.time() - start_time))
print(len(rolf.center), 'neurons approximating', len(X), 'datapoints')
print(len(np.unique(rolf.lables)), 'clusters where found')
print(silhouette_score(rolf.center, rolf.lables))
'''
##### Vizualizing learned Network ###############################################
'''
fig, (ax1, ax2) = plt.subplots(1, 2)

for c in range(0, len(rolf.center)):
    radius = rolf.sigma[c]*rolf.p
    circle = plt.Circle((rolf.center[c][0], rolf.center[c][1]),radius, alpha=0.15,)
    ax1.add_patch(circle)
    circle = plt.Circle((rolf.center[c][0], rolf.center[c][1]),rolf.sigma[c], alpha=0.25,)
    ax1.add_patch(circle)

    for k in range(0, len(rolf.center)):
        distance = np.linalg.norm(rolf.center[c] - rolf.center[k])
        perc = (rolf.sigma[c] + rolf.sigma[k])*rolf.p
        if distance <= perc:
            ax1.plot([rolf.center[c][0], rolf.center[k][0]], [
                    rolf.center[c][1], rolf.center[k][1]], linewidth=1, color='black')
ax1.scatter(X[:, 0], X[:, 1], marker='.', color="black", alpha=0.02)
ax1.set_title("network vizualization")

##### Vizualize input space clustering #############################################


labels = []
points = []
for x in np.arange(-50,50,1):
    for y in np.arange(-20,20,1):
        points.append([x,y])
        labels.append(rolf.predict([x,y]))
points = np.asarray(points)
labels = np.asarray(labels)

for i in np.unique(labels):
    cluster = points[labels==i]
    if i == -1:
        ax2.scatter(cluster[:,0],cluster[:,1],label='class: unknown')
    else:
        ax2.scatter(cluster[:,0],cluster[:,1],label='class: ' + str(i))

ax2.set_title("predicted clusters for the input space")
plt.show()
'''
'''
#3D Plots

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
labels = []
points = []
for x in np.arange(-50,50,0.1):
    for y in np.arange(-20,20,0.1):
        for z in np.arange(-20, 20, 0.1):
            print(type(x))
            print(type(y))
            print(type([x,y,z]))
            points.append([x,y,z])
            labels.append(rolf.predict([x,y,z]))
points = np.asarray(points)
print(points)
labels = np.asarray(labels)
print(labels)
for i in np.unique(labels):
    cluster = points[labels==i]
    if i == -1:
        plt.scatter(cluster[:,0],cluster[:,1],cluster[:,2],label='class: unknown')
    else:
        plt.scatter(cluster[:,0],cluster[:,1],cluster[:,2],label='class: ' + str(i))

plt.title("predicted clusters for the input space")
plt.show()

#plotting
'''
#Plotting PCA reduced Clusters
'''
rolf_PCA = PCA(n_components=2).fit_transform(rolf.center)
plt.scatter(rolf_PCA.T[0], rolf_PCA.T[1], c=rolf.lables)
plt.title('PCA reduced Clusters')
plt.ylabel('PCA_comp1')
plt.xlabel('PCA_comp0')
plt.show()
'''
'''
#decision tree on classification task
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(rolf_PCA, rolf.lables)
text_representation = tree.export_text(clf)
print(text_representation)

fig = plt.figure(figsize=(50,25))
_ = tree.plot_tree(clf,
                   feature_names=['PCA_comp0','PCA_comp1'],
                   class_names=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29'],
                   filled=True)


#clf DecisionTreeClassifier
import graphviz
# DOT data
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=['PCA_comp0','PCA_comp1'],
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png")
graph
#nochmal für gesamten Featureraum
'''
'''
def gentargetfile():
    with open('rolf.pickle', 'rb') as handle:
        ROLF = pickle.load(handle)
    X = pd.read_csv('hammerhead_reduced.csv', delimiter=',')
    X = X.fillna(0)
    del X['epoch']
    X = X.to_numpy()
    results = []
    for i in range(len(X)):
        results.append(ROLF.predict(X[i]))
    y = np.array(results)
    return y


clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, gentargetfile())
text_representation = tree.export_text(clf)
print(text_representation)

fig = plt.figure(figsize=(150,75),dpi = 200)
_ = tree.plot_tree(clf,filled=True)
fig.savefig("decistion_tree.png")
'''