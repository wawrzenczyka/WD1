# Uses SankeyMATIC.com to generate plot

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info.csv')
df

# %%
by_subpanel = df.groupby('subpanel')\
    .sum()\
    .reset_index(drop = False)\
    .loc[:, ['subpanel', 'budget']]

by_subpanel

# %%
df = df.assign(panel = df.subpanel.str.slice(start=0, stop=2))
by_panel = df.groupby('panel')\
    .sum()\
    .reset_index(drop = False)\
    .loc[:, ['panel', 'budget']]

by_panel

# %%
with open('data.txt', 'w+') as f:
    for index, row in by_panel.iterrows():
        f.write('Budżet' + ' [' + str(row['budget']) + '] ' + row['panel'] + '\n')
    for index, row in by_subpanel.iterrows():
        f.write(row['subpanel'][0:2] + ' [' + str(row['budget']) + '] ' + row['subpanel'] + '\n')

# %%
