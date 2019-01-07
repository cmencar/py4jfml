from py4j.java_gateway import JavaGateway
from py4jfml.Py4Jfml import Py4jfml

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

gateway = JavaGateway()

#%% load data
# import some data to play with
iris = datasets.load_iris()




#%% load FIS from FML file

fis = Py4jfml.load("IrisMamdani2.xml")
print(fis)


fis_output = []
for sample in iris.data:
    fis.getVariable("SepalLength").setValue(sample[0])
    fis.getVariable("SepalWidth").setValue(sample[1])
    fis.getVariable("PetalLength").setValue(sample[2])
    fis.getVariable("PetalWidth").setValue(sample[3])
    fis.evaluate()
    fis_output.append(fis.getVariable("irisClass").getValue())
    
    
#%% Train a svm from scikit-learn
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(iris.data, iris.target)
    svm_output=clf.predict(iris.data)

#%% display results
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
output = y
edge_colors = [('green' if svm_output[i]==int(fis_output[i]-1) else 'red') for i in range(len(y))]

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=output, cmap=plt.cm.Set1,
            edgecolor=edge_colors)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

##%% PCA
#
## To getter a better understanding of interaction of the dimensions
## plot the first three PCA dimensions
#fig = plt.figure(1, figsize=(8, 6))
#ax = Axes3D(fig, elev=-150, azim=110)
#X_reduced = PCA(n_components=3).fit_transform(iris.data)
#ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
#           cmap=plt.cm.Set1, edgecolor='k', s=40)
#ax.set_title("First three PCA directions")
#ax.set_xlabel("1st eigenvector")
#ax.w_xaxis.set_ticklabels([])
#ax.set_ylabel("2nd eigenvector")
#ax.w_yaxis.set_ticklabels([])
#ax.set_zlabel("3rd eigenvector")
#ax.w_zaxis.set_ticklabels([])
#
#plt.show()
