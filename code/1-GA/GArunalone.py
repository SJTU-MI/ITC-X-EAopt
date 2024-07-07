#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sko.GA import RCGA

with open('./data_ITC/SiGe_structure_ITC.txt', 'r') as SiGe_structure_ITC_file:
    SiGe_structure_ITC_lines = SiGe_structure_ITC_file.readlines()

with open('./data_ITC/SiSi_structure_ITC.txt', 'r') as SiSi_structure_ITC_file:
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
        result_list.append([str(len(structure_opt_list_all)), '\t', structure_str, '\t', str(ITC), '\n'])
#         print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return ITC


def SiGe_structure_opt_max(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiGe_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        result_list.append([str(len(structure_opt_list_all)), '\t', structure_str, '\t', str(ITC), '\n'])
#         print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return -ITC


def SiSi_structure_opt_min(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiSi_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        result_list.append([str(len(structure_opt_list_all)), '\t', structure_str, '\t', str(ITC), '\n'])
#         print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return ITC


def SiSi_structure_opt_max(struc):
    structure_list = process(struc)
    structure_str = ''.join(structure_list)
    ITC = SiSi_structure_ITC_dict[structure_str]
    if structure_str not in structure_opt_list_all:
        structure_opt_list_all.append(structure_str)
        result_list.append([str(len(structure_opt_list_all)), '\t', structure_str, '\t', str(ITC), '\n'])
#         print(len(structure_opt_list_all), '\t', structure_str, '\t', ITC)

    return -ITC


# In[2]:


for seed in range(0,50):
    resultlog_name = './result_'+ str(seed) + '.log'
    
    result_list = []
    structure_opt_list_all = []
    number_distinct_structures_set = 1000

    ga = RCGA(
        func=SiGe_structure_opt_max,
        size_pop=18,
        prob_cros=0.8,
        prob_mut=0.2,
        # fixed set
        n_dim = 16,
        lb=[0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0],
        ub=[2, 2, 2, 2,
            2, 2, 2, 2,
            2, 2, 2, 2,
            2, 2, 2, 2]
    )

    run_counts = 0
    run_max = 1000
    while len(structure_opt_list_all) < number_distinct_structures_set:
        if run_counts <= run_max:
            run_counts = run_counts + 1
            best_x, best_y = ga.run()
        else:
            break

    result_data = open(resultlog_name, mode='w')
    for resultline in result_list:
        result_data.writelines(resultline)
    result_data.close()
