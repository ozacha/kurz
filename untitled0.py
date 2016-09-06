# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:47:29 2016

@author: Ondra
"""

import pandas as pd
import matplotlib
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead
os.chdir('E:\\code\\python_course\\DAT210x')

student_dataset = pd.read_csv("Datasets/students.data", index_col=0)

my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2', 'G1']] 

my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)
