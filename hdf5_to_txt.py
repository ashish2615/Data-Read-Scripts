import numpy as np
import h5py
import pandas as pd
import deepdish


## open the data file
#injection_parameters =
#print(injection_parameters)
'''
injection_parameters = pd.read_hdf('/Users/ashish2615/Desktop/CBC_BH/injections_test.hdf5',mode = 'r')
# print(injection_parameters)
## Create a injection parameters file with txt format.
injection_file = open('injection_parameters.txt', mode = 'w')
## creating a numpy array of injection_paramters values
injection_parameters_values = injection_parameters.values()
#print(injection_parameters_values)
## saving data file to txt format
np.savetxt(injection_file, injection_parameters, delimiter=",")
injection_file.close()

injection_parameters.close()

'''

inj_param = np.load("/Users/ashish2615/Desktop/CBC_BH/outdir/injection_parameters_1.npy")
print(inj_param)
print(inj_param.item())
print(inj_param.item().values())
