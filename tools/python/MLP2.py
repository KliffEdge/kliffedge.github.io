from random import randint

import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing as pre
# from create_matrix import init_dir
import os

# for i in range(2):
#     path = os.getcwd()
#     parent = os.path.dirname(path)
#     os.chdir(parent)
# print(os.getcwd())
# os.chdir("data")
# data_dir = os.getcwd()
# print(data_dir)

matrix_lines = open("data/Matrix_of_Nations.txt").readlines()  # actions countries have taken
X_train = np.loadtxt( "data/Matrix_of_Nations.txt", delimiter=",")

y_lines = open( "data/y_train.txt").readlines()  # actions countries have taken
Y_train = np.loadtxt( "data/y_train.txt", delimiter=" ")
country_names =[]
f = open("data/countries_token.txt", "r")
for x in f:
  country_names.append(x.replace("\n", ""))

X_test = X_train[0:60]
Y_test = Y_train[0:60]
country_names_test = country_names[0:90]
X_train =X_train[60:180]
Y_train=Y_train[60:180]
country_names_train = country_names[90:180]

# y_rand = []
# y_train = []
# for _ in range(180):
#     y_rand.append(randint(0, 1000))
# y_rand = np.asarray(y_rand)

# for y in y_rand:
#     y = (y - np.min(y_rand)) / (np.max(y_rand) - np.min(y_rand))
#     y_train.append(y)
# y_train = np.asarray(y_train)

X_train.shape
Y_train.shape
num = 20000

mlp_model_exponential = MLPRegressor( solver='lbfgs' , max_iter=num,hidden_layer_sizes=(180,))
mlp_model_exponential.fit(X_train, Y_train)

mlp_pred_exp = mlp_model_exponential.predict(X_test) 



one = str(country_names_test[0])
two = country_names_test[77]

fig, (ax1, ax2) = plt.subplots(2)
ax1.margins(0,0)
# ax1.set_title(one, fontsize=16)
# ax1.plot(mlp_pred_exp[0],'m')
ax1.plot(mlp_pred_exp,'b')


ax2.margins(0,0)
# ax2.set_title(two, fontsize=16)
# ax2.plot(mlp_pred_exp[77],'m')
ax2.plot(Y_test,'b')
fig.show()
plt.show()
