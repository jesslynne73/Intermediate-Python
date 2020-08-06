# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:58:04 2020

@author: jstrait

This project will take NLP data including indicators for the presence of certain
concepts, segment the data by relevant variables, and produce correlation data 
between the presence of a concept and whether or not the claim was referred.

This is a condensed and data-free version of a correlation analysis script that 
I used for a project at MetLife. 
"""


## Front Matter
import pandas as pd
from pandas import *
from scipy import stats
from scipy.stats.stats import pearsonr


## Input data
data = pd.read_excel("insert file name here.xlsx")


## Data processing
# View only ended STD claims
data = data[data['CLM_STATUS'] == 'ENDED'].copy()
data = data[data['PROD_TYPE'] == 'STD'].copy()
# Subset data by duration
short = data[data['SHORT_LONG'] == 'SHORT']
long = data[data['SHORT_LONG'] == 'LONG']

## Calculating correlations from clinical referral indicator
correlations = {}
col_list = data.columns.tolist()
remove_cols = {'CLM_NUM_CD', 'SYS_DATA_TYP_CD', 'action_text_mapped_concepts', 'PROD_TYPE', 'CLM_STATUS', 'ACNT_DURATION', 'SHORT_LONG'}
var_list = [ele for ele in col_list if ele not in remove_cols] 

## Calculate correlations for unsegmented data
# Calculate correlations based on referral indicator
col_a = "REF_IND"
for entity in var_list:
     correlations[col_a + '__' + entity] = stats.pearsonr(data[col_a], data[entity])
     data_referral = pd.DataFrame.from_dict(correlations, orient='index')
data_referral.columns = ['ref_pearson_r', 'ref_p-value']

## Calculate correlations for duration segments
correlations = {}
# The metrics data frame tracks how many occurrences of a concept there are in the dataset
short_metrics = {}

for entity in var_list:
     correlations[col_a + '__' + entity] = stats.pearsonr(short[col_a], short[entity])
     short_ref = pd.DataFrame.from_dict(correlations, orient='index')
     short_metrics['{}'.format(entity)] = sum(short[entity])
short_ref.columns = ['short_ref_pearson_r', 'short_ref_p-value']
short_metrics = pd.DataFrame.from_dict(short_metrics, orient = 'index')
short_metrics.columns = ['short_count']

correlations = {}
long_metrics = {}

for entity in var_list:
     correlations[col_a + '__' + entity] = stats.pearsonr(long[col_a], long[entity])
     long_ref = pd.DataFrame.from_dict(correlations, orient='index')
     long_metrics['{}'.format(entity)] = sum(long[entity])
long_ref.columns = ['long_ref_pearson_r', 'long_ref_p-value']
long_metrics = pd.DataFrame.from_dict(long_metrics, orient = 'index')
long_metrics.columns = ['long_count']

metrics_table = pd.merge(short_metrics, long_metrics, left_index = True, right_index = True)

## Create table
data_dur_ref_table = pd.merge(data_referral, short_ref, left_index=True, right_index=True)
data_dur_ref_table = pd.merge(data_dur_ref_table, long_ref, left_index=True, right_index=True)

## Export data to an Excel file
writer = pd.ExcelWriter("desired file location.xlsx")
data_dur_ref_table.to_excel(writer, "Duration Segments")
metrics_table.to_excel(writer, "Metrics")
writer.save()

