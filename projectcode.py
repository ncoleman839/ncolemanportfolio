#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('Social_media_impact_on_life.csv')
data["Primary_Platform"].value_counts().plot(kind='bar')
data["Age"].min()
data["Age"].max()
data["Age"].value_counts().plot(kind='bar')

# %%
