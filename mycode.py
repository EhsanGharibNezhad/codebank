#here
# to IO/manipulate/calculate dataframes
import pandas as pd
import numpy as np

# to do math/statisctics
import statistics as stat
import math

# to vitualize data
import matplotlib.pyplot as plt
import seaborn as sns


# to do modeling with sklrean
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso, LassoCV


from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

# other packages
import warnings
warnings.filterwarnings(action='ignore')


# Printing Fuctions ------------------------------------------------

# Visualization Fuctions --------------------------------------------

# Modeling Fuctions ------------------------------------------------

# API Fuctions ------------------------------------------------

# Statiscics Functions ----------------------------------------
def replace_null_with_mean(data, feature_list):
    """
    Calculate the mean of each column in a dataset and replace nulls with the column's mean
    """
    [ data[feature].fillna(data[feature].mean(),inplace=True) for feature in feature_list ]
    
    

# Read Fuctions ------------------------------------------------

# Save Fuctions ------------------------------------------------
