import pandas as pd
import seaborn as sns
from pandas import HDFStore
import matplotlib.pyplot as plt

injections_data = pd.HDFStore('/Users/ashish2615/Desktop/CBC_3/injections_test.hdf5', mode = 'r')
print(injections_data)

for key in injections_data.keys():
    print('key : ' , key)            ## this will give the keys in the hdf5 data file
    injections_data_key_header = injections_data[key]         ## this will define the column heads of data frame and data with in the column i.e. data series. ## this will give me data store inside the key
    for keys in injections_data_key_header.keys():
        print(keys)                    ## this will print all column head within the dataframe for a given key
    print(injections_data_key_header)              ## this will print the whole data frame within the given key
    injections_data_type = type(injections_data.keys)          ## t = type
    #print(injections_data_type)
    injections_data_read = pd.read_hdf('/Users/ashish2615/Desktop/CBC_3/injections_test.hdf5', mode = 'r')
    #print(injections_data_read)
    print(injections_data_read.head())
    print(injections_data_read.columns)
    injections_data_mass_1 = injections_data_read.loc[ : , 'mass_1' : 'mass_1'] #injections_data.loc[:, '12': '13']
    #print( injections_data_mass_1)
    injections_data_mass_1_1 = injections_data_read.loc[  : 0 , 'mass_1' : 'mass_1']
    #print(injections_data_mass_1_1)
    #injections_data_value = injections_data_mass_1.values
    #print(injections_data_value)
    #print(injections_data_value.mean()) ## mean.
    #print(injections_data_value.std())  ## std deviation.
    #injections_data_read.close()
    #sns.violinplot(x='mass_1', data=injections_data_read, orient='h' , palette="muted")
    #plt.show()

injections_data_read.close()
injections_data.close()
