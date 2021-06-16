from __future__ import print_function
import os
from pathlib import Path
import math
import json
import numpy as np
from pprint import pprint
import pandas as pd

current_direc = os.getcwd()
print("Current Working Directory is :", current_direc)

def multi_det_subtracted_parameters():
    ## reading the max likelihood directory
    multi_det_max_likelihood = os.path.join(current_direc, 'multi_det_max_likelihood')
    multi_det_max_likelihood_data = os.listdir('multi_det_max_likelihood')
    multi_det_max_likelihood_data_select = [x for x in multi_det_max_likelihood_data if x.startswith('37')]

    ## for List of Keys.
    multi_det_subtracted_param_list = []
    ## For making a dict of all values and their keys.
    multi_det_subtracted_params_dict = []

    i = 0

    for multi_det_max_likelihood_data_direc in sorted(multi_det_max_likelihood_data_select):
        if i <= 10:
            multi_det_current_max_likelihood_data_direc = os.path.join(multi_det_max_likelihood, multi_det_max_likelihood_data_direc)

            multi_det_max_likelihood_sample_data_file_name = os.path.join(multi_det_current_max_likelihood_data_direc,
                                                                'sample_param_' + str(i) + '_result.json')

            ## Loading the datafile in reading mode.
            multi_det_max_likelihood_sample_data_file_open = json.load(open(multi_det_max_likelihood_sample_data_file_name))

            multi_det_max_likelihood_sample_data_file_open_read = multi_det_max_likelihood_sample_data_file_open['posterior']['content']

            key_list =  []
            dict ={}
            for sub_sub_keys in multi_det_max_likelihood_sample_data_file_open_read:
                # print('sub_sub_keys in sub_key content of main_key posterior of json data_file', sub_sub_keys)
                # print((multi_det_max_likelihood_sample_data_file_open_read [sub_sub_keys][-1]))

                key_list.append(sub_sub_keys)
                dict[sub_sub_keys] = multi_det_max_likelihood_sample_data_file_open_read[sub_sub_keys][-1]

            del (dict['log_likelihood'])
            del (dict['log_prior'])

            multi_det_subtracted_param_list.append(key_list)
            multi_det_subtracted_params_dict.append(dict)

            i += 1

    return multi_det_subtracted_params_dict


multi_detect_subtraction_param = multi_det_subtracted_parameters()
print(multi_detect_subtraction_param)



# detector_network_data_file =json.load(open('/Users/ashish2615/Desktop/CBC_BH_Multidetector_Network/outdir0/sample_param_1_result.json'))
# print(type(detector_network_data_file))
# # pprint(detector_network_data_file)
# ## Reading all main keys in the json data_file
# # for main_keys in detector_network_data_file:
# #     print('All main keys in the JSON data file are {}'.format(main_keys))
# #     print(type(main_keys))
# ## Reading keys in posterior main key in the json data_file
# # for keys in detector_network_data_file['posterior']:
# #     print('keys in one main key posterior of JSON data file are {}'.format(keys))
# #     print(type(keys))
# #     print(type(detector_network_data_file['posterior']))
# ## Reading the sub_sub_keys in sub_key content of main_key posterior  of json data_file
# key_list = []
# new_dict = {}
#
# for sub_sub_keys in detector_network_data_file['posterior']['content']:
#     print('sub_sub_keys in sub_key content of main_key posterior of json data_file', sub_sub_keys)
#     print(type(sub_sub_keys))
#     print(type(detector_network_data_file['posterior']['content']))
#     print(type(detector_network_data_file['posterior']['content'][sub_sub_keys]))
#     print((detector_network_data_file['posterior']['content'][sub_sub_keys][-1]))
#     # pprint(detector_network_data_file['posterior']['content'][sub_sub_keys])
#     # for vals in detector_network_data_file['posterior']['content'][sub_sub_keys]:
#     #     print('Values for key {} are {}'.format(sub_sub_keys,vals))
#     #     #max_vals = vals[-1]
#     #     print('max_likelihood values is {}'.format(max(vals)))
#     key_list.append(sub_sub_keys)
#     new_dict[sub_sub_keys] = detector_network_data_file['posterior']['content'][sub_sub_keys][-1]
#
# print(key_list)
# print(new_dict)
#
#
#

