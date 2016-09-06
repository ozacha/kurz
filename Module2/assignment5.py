import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
df = pd.DataFrame(pd.read_csv('Datasets/census.data', header=None))
df = df.drop(labels=[0],axis=1)
df = df.dropna(axis=0)
df.columns = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
df = df.dropna(axis=0)
df = df.drop(df[df['capital-gain'] == '?'].index)

# df[is.na(df.age)]
for col in ['age', 'capital-gain', 'capital-loss', 'hours-per-week'] :
    dt[col] = pd.to_numeric(dt[col], errors='coerce')
    
df = pd.get_dummies(df,columns=['education'])
df = pd.get_dummies(df,columns=['race'])
df = pd.get_dummies(df,columns=['vertebrates'])
df = pd.get_dummies(df,columns=['sex'])
#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..



#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). Think to yourself, does it generally
# make more sense to have a numeric type or a series of categories
# for these somewhat ambigious features?
#
# .. your code here ..



#
# TODO:
# Print out your dataframe
#
# .. your code here ..


