from __future__ import print_function
import sys
import os
from pathlib import Path
import numpy as np
import glob
import pandas as pd
import seaborn as sns
from pandas import HDFStore
import matplotlib.pyplot as plt




###################################################
''' Reading and Plotting Injection Data '''
###################################################

def injection_data(count):
    #print(count)
    current_dir = os.getcwd()
    data_direc = os.listdir('.')
    # print(data_direc)
    injection_data_file_select = [x for x in data_direc if x.endswith('hdf5')]
    # print(injection_data_file_select)
    injection_data_file_name = os.path.join(current_dir, 'injections_100_test.hdf5')
    # print(injection_data_file_name)
    injection_data_file_read = pd.read_hdf(injection_data_file_name, mode='r')
    print(injection_data_file_read)
    # print(injection_data_file_read)
    # print(injection_data_file_read.head())
    # print(injection_data_file_read.columns)
    injection_data_file_read_mass_1 = injection_data_file_read.loc[:, 'mass_1': 'mass_1']
    # print(injection_data_file_read_mass_1)
    injection_data_file_read_mass_1_value = injection_data_file_read_mass_1.values
    # print(injection_data_file_read_mass_1_value)
    injection_data_file_value = injection_data_file_read_mass_1.loc[count: count,
                                      'mass_1': 'mass_1']  # first mass_1 injection value.
    # print(injection_data_file_value)
    injection_data_file_value_values = injection_data_file_value.values
    # print(injection_data_file_value_values)
    # sns.violinplot(x='mass_1', data=injection_data_file_read, orient='h', palette="muted")
    # plt.show()
    # plt.savefig("injection_mass_1_value_" + 'count' + '.png')

    return injection_data_file_value_values

## Check for injection_data
#start = injection_data(0)
#print(start)

#########################################
''' Reading and Plotting Sample Data'''
#########################################

current_direc = os.getcwd()
#print('Current Working Directory is : {} '.format(current_direc))
data_direc = os.listdir('.')                  ## This will read current directory in which we are working.(/current_directory)
#print(data_direc)
## This will find the files starts with digit 32 in the current working directory.
sample_data_direc_select = [x for x in data_direc if x.startswith('32')]
#print(len(sample_data_direc_select))
#print(sorted(sample_data_direc_select))

count = 0
for sample_data_direc in sorted(sample_data_direc_select):
    if count <= len(sample_data_direc_select):

        # print(sample_data_file)                                                         ## This will give all data directories with in the current working directories
        current_direc_data_file = os.path.join(current_direc,
                                               sample_data_direc)  ## This  command will call the data directories.
        #print('Current Sample Data Direc is  {}'.format(current_direc_data_file))
        sample_data_file_name = os.path.join(current_direc_data_file,
                                             'label_result.h5')  ## This will call the data file with label 'label_result.h5'.
        #print('Sample Data File Name is  {}'.format(sample_data_file_name))
        ## Loading the datafile in reading mode.
        sample_data_file_open = pd.HDFStore(sample_data_file_name,
                                           'r')  ## This command will load the data file in read mode.
        # print('Sample Data file opened is {}'.format(sample_data_file_open))
        for keys in sample_data_file_open:  ## This command will read main keys and sub keys in the data file
            print(keys)
        sample_data_file_open_read = pd.read_hdf(sample_data_file_name, '/data/posterior')
        # print('Sample Data file read is {}'.format(sample_data_file_open_read))
        # print(data_read_file.head()) # head of the DataFrame.
        # print(data_read_file.columns # columns of Datafrma.
        # data_read_file_column = data_read_file.loc[-1 : , : ]
        sample_data_file_read_column_mass_1 = sample_data_file_open_read.loc[:, 'mass_1': 'mass_1']
        #print(sample_data_file_read_column_mass_1)
        sample_data_file_read_column_values = sample_data_file_read_column_mass_1.values
        print(sample_data_file_read_column_values)
        injection_data_file_value = injection_data(count)
        print('mass_1 value for injection is {}'.format(injection_data_file_value))

        ################################################################
        ''' Subtracting ((M_sample - M_(best_fit)) - M_injected ) '''
        ################################################################

        subtracted_mass_1_value = (sample_data_file_read_column_values - injection_data_file_value)
        print('Subtracted mass_1_value are {}'.format(subtracted_mass_1_value))
        sns.violinplot(x = subtracted_mass_1_value, orient='h', inner = 'box' , palette = 'RdBu_r')
        plt.savefig("subtracted_mass_1_neagtive_value_{}.png".format(count))
        plt.show()

        #sns.violinplot(x='mass_1', data=sample_data_file_open_read, orient='h', palette="Set2", inner='quartile',hue='mass_1')
        #plt.savefig("sample_mass_1_value_{}.png".format(count))
        #plt.show()

    count += 1


#sample_data_file_open_read.close()
#sample_data_file_name.close()


