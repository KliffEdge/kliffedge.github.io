from random import randint

import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib
import matplotlib.pyplot as plt
# from create_matrix import init_dir
import os

for i in range(2):
    path = os.getcwd()
    parent = os.path.dirname(path)
    os.chdir(parent)
print(os.getcwd())
os.chdir("data")
data_dir = os.getcwd()
print(data_dir)

matrix_lines = open(data_dir + "/Matrix_of_Nations.txt").readlines()  # actions countries have taken
X_train = np.loadtxt(data_dir + "/Matrix_of_Nations.txt", delimiter=",")

y_rand = []
y_train = []
for _ in range(180):
    y_rand.append(randint(0, 1000))
y_rand = np.asarray(y_rand)

for y in y_rand:
    y = (y - np.min(y_rand)) / (np.max(y_rand) - np.min(y_rand))
    y_train.append(y)
y_train = np.asarray(y_train)

print(X_train.shape)
print(y_train.shape)

mlp_model_exponential = MLPRegressor(solver='lbfgs')
mlp_model_exponential.fit(X_train, y_train)
mlp_pred_exp = mlp_model_exponential.predict(X_train)
print((mlp_pred_exp-y_train)**2)
plt.plot(y_train,(mlp_pred_exp-y_train)**2)
plt.show()