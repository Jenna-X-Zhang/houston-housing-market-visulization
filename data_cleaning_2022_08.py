#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For visulization project 
hotness data on zipcode level
all zipcodes in houston metro ara are aggregated
"""

#pip install yfinance 准备环境
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date
from datetime import datetime 
from scipy import stats
today = datetime.today()
curr_month = datetime(today.year, today.month, 1)
pd.options.mode.chained_assignment = None
#%% Manipulate data

# import the 
historical_hotness= pd.read_csv(r'/Users/xuan/Dropbox/1Research_Projects/investment/housing/visualization/RDC_Inventory_Hotness_Metrics_Zip_History.csv')

historical_hotness[['zip_name', 'state']] = historical_hotness['zip_name'].str.split(',', expand=True) 

houston_area_zipcode = ['bellaire','cypress','fresno','frendswood','houston','humble','katy','missouri city','pasadena','pearland','richmond','rosenberg','stafford','sugar land','webster']

houston_hotness_historical = historical_hotness[historical_hotness['zip_name'].isin(houston_area_zipcode)] 

houston_hotness_historical = houston_hotness_historical[houston_hotness_historical['state'].str.contains('tx')]

houston_hotness_historical['zip_name'].value_counts()

df = houston_hotness_historical.groupby(['zip_name','month_date_yyyymm'])[['nielsen_hh_rank','hotness_rank', 'hotness_rank_mm', 'hotness_rank_yy', 'hotness_score','supply_score', 'demand_score', 'median_days_on_market',  'median_days_on_market_mm', 'median_dom_mm_day', 'median_days_on_market_yy', 'median_dom_yy_day', 'median_dom_vs_us',       'ldp_unique_viewers_per_property_mm', 'ldp_unique_viewers_per_property_yy', 'ldp_unique_viewers_per_property_vs_us', 'median_listing_price',     'median_listing_price_mm', 'median_listing_price_yy',      'median_listing_price_vs_us','quality_flag']].median()

# df.to_csv('houston_hotness_2022_08.csv')
















