from random import randint

import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib
import matplotlib.pyplot as plt
from sklearn.ensemble._forest import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
# from create_matrix import init_dir
import os
# Set a seed value
seed_value= 0
# 1. Set `PYTHONHASHSEED` environment variable at a fixed value
import os
os.environ['PYTHONHASHSEED']=str(seed_value)
# 2. Set `python` built-in pseudo-random generator at a fixed value
import random
random.seed(seed_value)
# 3. Set `numpy` pseudo-random generator at a fixed value
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

# y_rand = []
# y_train = []
# for _ in range(180):
#     y_rand.append(randint(0, 1000))
# y_rand = np.asarray(y_rand)

# for y in y_rand:
#     y = (y - np.min(y_rand)) / (np.max(y_rand) - np.min(y_rand))
#     y_train.append(y)
# y_train = np.asarray(y_train)


X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.2, random_state=0)


np.random.seed(seed_value)
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(len(y_pred))
# num = 2000000
# for i in range(20):
#     # mlp_model_exponential = MLPRegressor( solver='lbfgs' , max_iter=num)
#     # mlp_model_exponential.fit(X_train, Y_train)
#     random.seed(100)
#     rf = RandomForestClassifier(n_estimators=1000)  

# rf.fit(X_train, Y_train)
# mlp_pred_exp= rf.predict(X_train)
#mlp_pred_exp = mlp_model_exponential.predict(X_train) 
num = 0
mlp_pred_exp = y_pred[num]

# print((mlp_pred_exp-Y_train)**2)
# plt.plot(Y_train,(mlp_pred_exp-Y_train)**2)
plt.plot(mlp_pred_exp)

plt.show()