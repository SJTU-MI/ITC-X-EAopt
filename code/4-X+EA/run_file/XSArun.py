#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from SA import SA
import os

######################################################
with open('./data_ITC/SiGe_structure_ITC.txt', 'r') as SiGe_structure_ITC_file:
######################################################
    SiGe_structure_ITC_lines = SiGe_structure_ITC_file.readlines()

######################################################
with open('./data_ITC/SiSi_structure_ITC.txt', 'r') as SiSi_structure_ITC_file:
######################################################
    SiSi_structure_ITC_lines = SiSi_structure_ITC_file.readlines()

SiGe_structure_ITC_dict = {}
SiSi_structure_ITC_dict = {}

for SiGe_structure_ITC_line in SiGe_structure_ITC_lines:
    line = SiGe_structure_ITC_line.strip()
    columns = line.split()
    if len(columns) == 2:
        string_data = columns[0]
        float_data = float(columns[1])
        SiGe_structure_ITC_dict[string_data] = float_data

for SiSi_structure_ITC_line in SiSi_structure_ITC_lines:
    line = SiSi_structure_ITC_line.strip()
    columns = line.split()
    if len(columns) == 2:
        string_data = columns[0]
        float_data = float(columns[1])
        SiSi_structure_ITC_dict[string_data] = float_data


def struc_str2struc_atom_16_list(struc_str):
    struc_atom_16_list = []
    for atomindex, atom in enumerate(struc_str):
        struc_atom_16_list.append(int(atom))
    return struc_atom_16_list


def find_initial_struc():
    optfolder_path = './'
    resultfile_path = os.path.join(optfolder_path, '1optresult.log')

    ITC_value_list = []
    struc_list = []
    with open(resultfile_path, 'r') as resultlog:
        resultlog_lines = resultlog.readlines()

    for index, line in enumerate(resultlog_lines):
        ITC_value_list.append(float(line.split()[0]))
        struc_list.append(str(line.split()[1]))

    BO_ITC_value_list = ITC_value_list[:BO_search_counts]
    BO_struc_list = struc_list[:BO_search_counts]

    sorted_indices = np.argsort(BO_ITC_value_list)[::-1]
    top_indices = sorted_indices[:1]
    top_strucs = [BO_struc_list[i] for i in top_indices]
    initial_list = struc_str2struc_atom_16_list(top_strucs[0])

    return initial_list

def process(optlist):
    sorted_result = sorted(enumerate(optlist), key=lambda x: x[1], reverse=True)
    rank_index = [tup[0] for tup in sorted_result[:8]]
    result = ['1' if atom in rank_index else '0' for atom in range(0, 16)]
    return result


def SiGe_structure_opt_min(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiGe_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return ITC


def SiGe_structure_opt_max(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiGe_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return -ITC


def SiSi_structure_opt_min(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiSi_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return ITC


def SiSi_structure_opt_max(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiSi_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return -ITC


# In[2]:


structure_opt_list_all = []
###########################################################
BO_search_counts = 100
###########################################################
current_path = './'
ini_optresult_path = os.path.join(current_path, '1optresult.log')

load_struc_list = []
with open(ini_optresult_path, 'r') as ini_optresult_log:
    ini_optresult_log_lines = ini_optresult_log.readlines()

for index, ini_optresult in enumerate(ini_optresult_log_lines[:BO_search_counts]):
    SiSi_structure_opt_max(str(ini_optresult.split()[1]))


sa = SA(
    ######################################################
    func = SiSi_structure_opt_max,
    ######################################################
    x0 = find_initial_struc(),
    T_max = 100,
    T_min = 1e-7,
    L = 18,
    max_stay_counter = 60,
    m = 1.0,
    n = 1.0,
    quench = 0.5,
    lb = [0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0],
    ub = [2, 2, 2, 2,
          2, 2, 2, 2,
          2, 2, 2, 2,
          2, 2, 2, 2]
)

best_x, best_y = sa.run()
