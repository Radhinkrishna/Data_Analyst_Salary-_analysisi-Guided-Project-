# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:17:54 2023

@author: radhinkrishna
"""

import Data_scraping as ds
import pandas as pd
path=r"C:/Users/radhinkrishna/OneDrive/Desktop/Data_Analyst_Salary-_analysisi-Guided-Project-/Data Scraping/chromedriver.exe"
df=ds.get_jobs('data scientist',1000,False,path,15)
df.to_csv('glassdoor_jobs.csv', index = False)