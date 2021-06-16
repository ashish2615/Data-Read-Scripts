from __future__ import print_function
import os
from pathlib import Path
import glob
import pandas as pd


home = os.path.expanduser('~')                          ## This will read home directory address.
print('Home Directory is :{}'.format(home))
## OR ##
#print(Path.home())                                     ## One line command to read home directory address.

## Current working directory (cwd) for python
#cwd = os.getcwd()
#print(cwd)
## OR ##
current_direc = os.getcwd()          ## This will give current working directory
print('Current Working Directory is : {} '.format(current_direc))

#path1 = os.path.dirname(Path.home())                   ## This will read the directory in the home.
#print(path1)
#path = os.path.join(Path.home(), 'Desktop', 'CBC_BH')  ## Adding the directories to the home directory.
#print(path)
#location = os.path.join(Path.home(), "Desktop")
#print(location)
#folder_check = os.path.isdir(location)  ## Check if location is directory or not.
#print(folder_check)

list = os.listdir('..')                  ## This will list main_directory in which current directory lies.(/main_direcotry/current_directory)
print(list)
files = os.listdir('.')                  ## This will read current directory in which we are working.(/current_directory)
print(files)
'''
for filename in files:
    print(filename)
    if os.path.isfile(filename):
        print("{} is a file".format(filename))
    elif os.path.isdir(filename):
        print('{} is a directory'.format(filename))
    elif os.path.islink(filename):
        print('{} is a link'.format(filename))
    else:
       print('.-.-.-.-.')
'''
#############################################
## Finding Files with in the main directory
#############################################
## Iterator method
#data_file_select = filter[lambda x: x.startswith('32'), files] #didn't work
## Comprehension
data_file_select = [x for x in files if x.startswith('32')]        ## use this one.
## This will find the files starts with digit 32 in the current working directory.
print(sorted(data_file_select))        ## Printing the data directories in the sorted form.

#### Or Use this one ######
### importing data. This command can also be used.
#data_hdf = glob.glob('32*')
#print(sorted(data_hdf))
#print(sorted(glob.glob('3*')))              ## sort the data.

### reading the datafiles.

for data_file_hdf in sorted(data_file_select):
    #print(data_file_hdf)                         ## This will give all data directories with in the current working directories
    current_direc_data_file = os.path.join(current_direc, data_file_hdf )       ## This  command will call the data directories.
    #print(current_direc_data_file)
    file_name = os.path.join(current_direc_data_file,'label_result.h5')        ## This will call the data file with label 'label_result.h5'.
    #print(file_name)

    ## Check for path, if exist or not.
    #file_name_check_path = os.path.exists(file_name)
    #print(file_name_check_path)

    ## Loading the datafile in reading mode.
    file_open_read = pd.HDFStore(file_name,'r')     ## This command will load the data file in read mode.
    #print(file_open_read)
    for keys in file_open_read:           ## This command will read main keys and sub keys in the data file
        print(keys)
    file_open_read.close()                ## Close the data file to prevent it for corrput.


##################
#      END       #
##################

'''
topdir =''
exten = '.hdf5'
for names in current_direc_data_file:
    if name.lower().endswith(ext):
        print('os.path.join(dirname,name)')
'''

'''
def folder_name():
    # Get the home directory
    home = os.path.expanduser('~')
    folder_name_input = input('Type in folder name to check  : {}\\'.format(home))
    directory_check(home, folder_name_input)

def directory_check(home, folder):
    folder_path = os.path.join(home, folder)   ## check for the folder
    folder_check = os.path.isdir(folder_path)  ## check for the directory
    if folder_check is True:
        print("{} is a valid directory".format(folder_path))
        request_go_again()
    else:
        print("{} is not a valid directory".format(folder_path))
        request_go_again()

def request_go_again():
    go_again = input ('Check for another folder? (y/n): ')
    print(go_again)
    if go_again[:1] is 'y' or go_again[:1] is 'Y':
        redo = folder_name()
    elif go_again[:1] is 'n' or go_again[:1] is 'N':
         print('Bye Bye')
    else:
         print("Please Choose 'y' or 'n'")
         request_go_again()

print('Check if folder exist for user home directory or not. \n'
      'Input a folder')

## Start the process
start_check = folder_name()
'''

