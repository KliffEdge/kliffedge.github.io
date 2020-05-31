import numpy as np
import pandas as pd
measures = [[1,0,0],[0,0,1],[1,1,1],[1,0,1]]
spread = [[24,18],[5,23],[56,23],[7,2]]
print()

from sklearn.neural_network import MLPClassifier
#create mlp classifier
mlp = MLPClassifier(activation='logistic', solver='sgd', tol=0,learning_rate_init=.08, max_iter=200)

# fit network here
mlp.fit(measures,spread)
# predict categories of training data here
predictions = mlp.predict(measures)

assert(predictions == spread)


#Now using a perceptron:
from sklearn.linear_model import Perceptron
# Create Perceptron
perceptron = Perceptron()
# Fit network to the data X_train and y_train
perceptron.fit(measures, spread)
# Make predictions on the random data
perceptron_test_predictions = perceptron.predict(measures)

assert(perceptron_test_predictions == spread)


#MSE_runs = []  # create a list to store each result
#Is training it multiple times actually necessary since it's the same exact data?
#for i in range(10):  # iterate 10 times
#    mlp = MLPClassifier(activation='logistic', solver='sgd', tol=0,learning_rate_init=.08, max_iter=200)          #  recreate model
#    mlp.fit(measures, spread) #  fit model to training data (X_train, y_train)
#    predictions =  mlp.predict(measures) # predictions
#
#    MSE = mean_squared_error(predictions,spread)  #  compute MSE
#    MSE_runs.append(MSE)  # this stores the result of one run to the MSE_runs array
#print(MSE_runs)


#It could generate random measure matrices and predict their spread, but we would have no way of verifying it other than logic
#generate say 1000 random measures matrices here as X_test

#𝑁  random binary patterns, in 0/1 representation, with probability/sparseness 𝑠 for a 1 and probability 1−𝑠 for 0, for 𝑀 neurons
def make_patterns(N, M, s):
    #np.random.seed(42) # we fix the random seed to have reproducible results
    patterns = []
    for n in range (N):
        temp = np.asarray(np.random.rand(M))
        patterns.append(temp)
        
    patterns1 = []
    
    for n in range (N):
        temp1 = []
        for m in range (M):
            if patterns[n][m] <= s:
                temp1.append('1')
            else: 
                temp1.append('0')
        patterns1.append(temp1)
    
    return patterns1

X_test = make_patterns(100, 34, 0.5) #makes 100 patterns of 'measures'



# Make predictions on the random data
perceptron_test_predictions = perceptron.predict(X_test)

# predict categories of random data here
predictions = mlp.predict(X_test)