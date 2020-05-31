import pandas as pd
import numpy as np
import os


def init_dir():
    """
    Used to change the directory to data directory in kliffedge.github.io/data
    """
    for i in range(2):
        path = os.getcwd()
        parent = os.path.dirname(path)
        os.chdir(parent)
    print(os.getcwd())
    os.chdir("data")


def param_list():
    """
    Gets the list of parameters in measures_by_parameters

    :return parameters which is a list of parameters in measures_by_parameters.txt
    """
    data_dir = os.getcwd()
    measures_by_parameter = open(data_dir + "/measures_by_parameters.txt")
    lines = measures_by_parameter.readlines()
    required_lines = [0, 3, 4]  # As we only need lines 1,4,5 from measures_by_parameters
    parameters = []
    for line_num in required_lines:
        for param in (lines[line_num][1:-2].split(",")):
            parameters.append(param)
    return parameters


init_dir()

country_parameters = open(os.getcwd() + "/measures_by_country.txt")
matrix = []
cp_lines = country_parameters.readlines()
for line in cp_lines:
    row_of_matrix = []
    for param in param_list():
        if param in line:
            row_of_matrix.append(1)
        else:
            row_of_matrix.append(0)
    matrix.append(row_of_matrix)

np.savetxt("Matrix_of_Nations.txt",np.asarray(matrix), fmt='%i',delimiter=',')
df = pd.DataFrame(np.asarray(matrix), columns=param_list())
print(os.getcwd())
df.to_csv(os.getcwd()+"matrix.csv")