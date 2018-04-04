import matplotlib
import matplotlib.pylot as plt
import numpy as np
import pandas
import sklearn

# Load data
oecd = pandas.read_csv("oecd_bli_2015.csv", thousands=',')
gdp = pd.read_csv(
        "gdp_per_capita.csv", thousands=',', delimiter='\t',
        encoding='latin1', na_values="n/a"
    )

# Prepare the data
