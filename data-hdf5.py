import h5py
import numpy as np
import matplotlib.pyplot as plt


# Reading the hdf5 file
data = h5py.File('/Users/ashish2615/Desktop/CBC_3/33025138/sample_param_1_result.h5', 'r')
print(data)

# studing the structure of file/main groups/key by printing what hdf5 main group are present
for key in data.keys():
    print('main_keys :', key)  ## Names of the main key in HDF5 file. here we have only one main key named as data.

## Extracting the group within main data key.
group = data[key]
for key in group.keys():   ## Checkout what keys/sub-groups are inside that main group.
    print('group_key : ', key)

#subgroup = group[key]
#for keys in subgroup.keys():
#    print('sub_group_keys :', keys)

dataset_samples = group['samples'].value
print(dataset_samples)

print(dataset_samples[:, 1:2])
plt.hist(dataset_samples[:, 1:2], 1000, density =1)
plt.show()
plt.clf()

print(dataset_samples[:, 3:])
plt.hist(dataset_samples[:, 3:], 50, density = 1)
plt.show()
plt.clf()



'''
# studing the structure of file/main groups by printing what hdf5 main group are present
lst_key = list(data.keys())    ## This will produce a list of main dataset keys in hdf5 file.
print(lst_key)
dataset = data.get("data")   ## This will show how many number of group members in the main data key.
print(dataset)
#print(data['data'].keys())
lst_dataset = list(dataset)    ## This will produce a list of all groups members in the main data key of hdf5 file.
#print(lst_dataset)                

###################################
### detail process of reading the data
###################################
dataset = data.get('data')
#print(data)
#list_ = list(dataset)
dataset1 = group.get('posterior')
#print(dataset1)
#list_1 = list(dataset1)
#print(list_1)
dataset2 = group.get('posterior/block0_values')
#print(dataset2)
dataset3 = np.array(dataset2)
#print(dataset3)
print('Shape of block0_values', dataset2.shape)
dataset4 = list(dataset3)
print('Items in dataset2 are : ', dataset4)

'''

#dataset_posterior = data.get('data/posterior/block0_values')  # this will call main group then will call subgroup within the main group and then sub-subgroup.
#print(dataset_posterior)
#dataset1 = np.array(dataset_posterior) # defined value of data
#print("Shape of posterior/block0_values is  : ", dataset1.shape)
#dataset2 = list(dataset_posterior)
#print('Items in dataset2 are : ', dataset2)

data.close()


