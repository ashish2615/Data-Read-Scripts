import pandas as pd
import seaborn as sns
from pandas import HDFStore
import matplotlib.pyplot as plt

## basic completion : control+space
## smart completion : control+shift+space
## view references  : option+space

## Method : 1. This will not work if the HDF5 file has multiple datasets inside. It will raise a ValueError stating
# that the file has HDF file contains multiple datasets.
# df = pd.read_hdf('/Users/ashish2615/Desktop/BBH_final/outdir_1_0.09/label_1_0.09_result.h5', key = '", mode = 'r')

## Method : 2. Use this for multiple dataset.
hdf = pd.HDFStore('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775320/label_result.h5', mode = 'r') # mode = 'r'
print(hdf)
for key in hdf.keys():
    print('key : ' , key)            ## this will give the keys in the hdf5 data file
    hdf_key_header = hdf[key]         ## this will define the column heads of data frame and data with in the column i.e. data series. ## this will give me data store inside the key
    for keys in hdf_key_header.keys():
        print(keys)                    ## this will print all column head within the dataframe for a given key
    print(hdf_key_header)              ## this will print the whole data frame within the given key
    hdf_type = type(hdf.keys)          ## t = type
    print(hdf_type)

## Extracting a particular data
df1 = pd.read_hdf('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775320/label_result.h5', key = '/data/posterior' , mode = 'r')
df2 = pd.read_hdf('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775321/label_result.h5', key = '/data/posterior' , mode = 'r')
df3 = pd.read_hdf('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775322/label_result.h5', key = '/data/posterior' , mode = 'r')
df4 = pd.read_hdf('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775323/label_result.h5', key = '/data/posterior' , mode = 'r')

# df1['mass_1'].plot.hist()   ## This method only work for histogram and box plots.
# df2['mass_1'].plot.hist()

## slicing of columns , selecting first four.
df1_columns_4 = df1.loc[:, 'iota' : 'luminosity_distance']
#print(df1_columns_4)
# slicing for particular data series
df1_mass_1 = df1.loc[:, 'mass_1' : 'mass_1']
df1_value = df1_mass_1.values

##  Mass Difference
df1_diff = df1_mass_1.values

#print(df1_mass_1)
#print(df1_m1_value)
#print(df1_m1_value.size)
df2_mass_1 = df2.loc[:, 'mass_1' : 'mass_1']
df3_mass_1 = df3.loc[:, 'mass_1' : 'mass_1']
df4_mass_1 = df4.loc[:, 'mass_1' : 'mass_1']

'''
def hist(
        x, bins = None, range=None, density=None, weights=None,
        cumulative=False, bottom=None, histtype='bar', align='mid',
        orientation='vertical', rwidth=None, log=False, color=None,
        label=None, stacked=False, normed=None, *, data=None,
        **kwargs):
    return gca().hist(
        x, bins=bins, range=range, density=density, weights=weights,
        cumulative=cumulative, bottom=bottom, histtype=histtype,
        align=align, orientation=orientation, rwidth=rwidth, log=log,
        color=color, label=label, stacked=stacked, normed=normed,
        **({"data": data} if data is not None else {}), **kwargs)
'''

#df-mass_1_plot = df.mass_1.value_counts().plot(kind = 'hist')
#plt.hist(df1_mass_1.values, 500)
#plt.hist(df2_mass_1.values, 500)
#plt.hist(df3_mass_1.values, 500)
#plt.hist(df4_mass_1.values, 500)

## Violine plot using matplotlib for multiple datasets.
#plt.violinplot(dataset = ((df1_mass_1.values),(df2_mass_1.values),(df3_mass_1.values),(df4_mass_1.values)), positions = [1,2,3,4], vert = True, widths = 2.0, points = 6)
#plt.xlabel('Position of masses')
#plt.ylabel('Masses{m_1, m_2, m_3, m_4}')
#plt.title('Violin Plot for Four Injections m_1 Mass Term')
#plt.show()
#plt.clf()

## Pairplot for dataframe using seaborn
#sns.pairplot(df4)

## PairGrid plot using seaborn
#g = sns.PairGrid(df4)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)
#g.map_diag(sns.kdeplot, lw = 3, legend = False)


#########################
#########################

   # Using Seaborn #

##########################
##########################

#### For single data series violin plot using sns.violineplot.
# sns.violinplot(x = df1.loc[:, 'mass_1' : 'mass_1'], data = df1, orient = 'v', hue = 'mass_1', palette="muted", split=True, scale="count")

## OR ##

### Violine plot using single data file.


#sns.factorplot(x = 'mass_1', hue = 'Kind', Kind = 'violin', data = df2)
#plt.show()

#sns.violinplot


df5 = pd.read_hdf('/Users/ashish2615/Desktop/Djobs/BBH_SNRinj/32775324/label_result.h5', key = '/data/posterior', mode = 'r')
## Initializing  figure and axes objet.
#fig = plt.subplot()
## using default seaborn
#sns.set()   # explicitly use sns.set() to turn on the seaborn styles
sns.set(style="whitegrid")
sns.violinplot(x = 'mass_1', data = df5, orient = 'h', palette = 'Pastel1', scale = 'count', scale_hue = False,  inner='box', split=True, bw= 1) #, legend=False)  # gridsize=1000,cut=0
sns.violinplot(x = 'mass_1', data = df4, orient = 'h', palette = "muted",   scale = 'count', scale_hue = False,  inner='box', split=True, bw= 1)
sns.violinplot(x = 'mass_1', data = df3, orient = 'h', palette = "Blues",   scale = 'count', scale_hue = False,  inner='box', split=True, bw= 1)
sns.violinplot(x = 'mass_1', data = df2, orient = 'h', palette = "muted",   scale = 'count', scale_hue = False,  inner='box', split=True, bw= 1)
sns.violinplot(x = 'mass_1', data = df1, orient = 'h', palette = "muted",   scale = 'count', scale_hue = False,  inner='box', split=True, bw= 1)
#sns.despine(left=True)
#order = ('df5', 'df4', 'df3', 'df2', 'df1')
#hue_order = ('df1', 'df2', 'df3', 'df4', 'df5')
plt.show()
#plt.clf()


'''
## This one can also be used to check keys.
hdf_keys = hdf.keys() # this command will give the keys within the hdf5 datafile.
print(hdf_keys) or print(hdf.keys())                     ## this will print main keys within hdf5 data file.
keys_in_key1 = hdf['/data/nested_samples'].keys()
keys_in_key2 = hdf['/data/posterior'].keys()
print(keys_in_key1)
print(keys_in_key2)
##  Note this command will show keys in main data key which further have subfolders of data files.
# like in main data key nested_samples and data/posterior have further sub data files within them whereas rest files do not have.
# That is why only these two keys will be print by hdf_keys command.
'''

hdf.close()



