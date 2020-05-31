from random import randint

import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing as pre
import os
import csv

#X
X =[]
X_token =[]
with open("tools/python/comparative_tools/data/data_moblity_train.csv") as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')

  for x in readCSV:
    X.append(x)

print(X)
with open("data/countries_token_mobility.txt") as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')

  for x in readCSV:
    x = x[0]
    X_token.append(x)
#Y

Y = np.loadtxt( "tools/python/comparative_tools/data/y_train.txt", delimiter=" ")
print(Y)

X_test = X[0:63]
Y_test = Y[0:63]
X_test_tokens = X_token[0:63]
X_train =X[63:127]
Y_train=Y[63:127]
X_train_tokens = X[63:127]


mlp_model_exponential = MLPRegressor( solver='lbfgs')
mlp_model_exponential.fit(X_train, Y_train)

mlp_pred_exp = mlp_model_exponential.predict(X_test)

plt.plot(mlp_pred_exp)
plt.plot(Y_test)
plt.show()