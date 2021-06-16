from __future__ import print_function
import os
from pathlib import Path
import glob
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import HDFStore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


current_direc = os.getcwd()
print('Current Working Directory is : {} '.format(current_direc))

list = os.listdir('..')                  ## This will list main_directory in which current directory lies.(/main_direcotry/current_directory)
print(list)
files = os.listdir('.')                  ## This will read current directory in which we are working.(/current_directory)
print(files)

## This will find the files starts with digit 32 in the current working directory.
data_file_select = [x for x in files if x.startswith('32')]
print(sorted(data_file_select))

for data_file_hdf in sorted(data_file_select):
    #print(data_file_hdf)
    current_direc_data_file = os.path.join(current_direc, data_file_hdf )
    #print(current_direc_data_file)
    file_name = os.path.join(current_direc_data_file,'label_result.h5')
    #print(file_name)
    ## Loading the datafile in reading mode.
    file_open_read = pd.HDFStore(file_name,'r')
    #print(file_open_read)
    for keys in file_open_read:
        print(keys)
    data_read_file = pd.read_hdf(file_name,'/data/posterior')
    #print(data_read_file)
    # print(data_read_file.head()) # head of the DataFrame.
    # print(data_read_file.columns # columns of Datafrma.
    #data_read_file_column = data_read_file.loc[-1 : , : ]
    data_read_file_column = data_read_file.loc[:, 'mass_1' : 'mass_1']
    #print(data_read_file_column)
    data_read_file_column_value = data_read_file_column.values
    print(data_read_file_column_value)
    #data_read_file.close()
    # violin plot and save plots
    sns.set(style="ticks")
    #fig, ax = plt.subplots(4,4, figsize = (8,4)) # didn't work.
    sns.violinplot(x='mass_1', data=data_read_file, orient='h', palette='Pastel1', scale='count', scale_hue=False,
                   inner='box',
                   split=True, bw=1)
    '''
    for mass_1 in data_read_file:
        sns.violinplot(x='mass_1', data = data_read_file, orient='h', palette='Pastel1', scale='count', scale_hue=False,
                       inner='box',
                       split=True, bw=1)
    '''
    plt.show()
    file_open_read.close()



