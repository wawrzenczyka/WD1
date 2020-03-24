# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info.csv')
df['sex'] = np.where(df.sex == 1, 'Male', 'Female')

# %%
budget_per_voivodeship = df\
    .groupby('voivodeship')\
    .mean()\
    .budget\
    .rename('budget')\
    .reset_index(drop = False)\
    .sort_values('budget', ascending = False)
ax = sns.barplot(x = 'voivodeship', y = 'budget', \
    data = budget_per_voivodeship)
ax.set_xticklabels(ax.get_xticklabels(), \
    rotation=45, horizontalalignment='right')

# %%
count_per_voivodeship = df\
    .groupby('voivodeship')\
    .size()\
    .rename('count')\
    .reset_index(drop = False)\
    .sort_values('count', ascending = False)
ax = sns.barplot(x = 'voivodeship', y = 'count', \
    data = count_per_voivodeship)
ax.set_xticklabels(ax.get_xticklabels(), \
    rotation=45, horizontalalignment='right')

# %%
import geopandas as gpd
import os

pl_voi = gpd.read_file('Województwa.shp', encoding = 'UTF-8')

# # %%
# pl_voi.head()

# # %%
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots(1, figsize=(14, 14))
# pl_voi.plot(ax=ax, linewidth=0.5, edgecolor='0.4', \
#     color='0.8')
# ax.axis('off')

# %%
pl_voi_count = pl_voi.merge(count_per_voivodeship, \
    left_on = 'JPT_NAZWA_',\
    right_on = 'voivodeship')
    
fig, ax = plt.subplots(1, figsize=(8, 8))

from mpl_toolkits.axes_grid1 import make_axes_locatable

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

pl_voi_count.plot(ax=ax, edgecolor='0.0', linewidth=0.5, 
                  column='count', cmap='Reds', cax=cax,
                  legend=True, 
                  legend_kwds={'label': "Grant count"})

# ax.set_aspect('equal')
ax.set_aspect(4./3)
ax.axis('off')
plt.savefig('grant_count_map.svg', format = 'svg')


# %%
pl_voi_budget = pl_voi.merge(budget_per_voivodeship, \
    left_on = 'JPT_NAZWA_',\
    right_on = 'voivodeship')
    
fig, ax = plt.subplots(1, figsize=(8, 8))

from mpl_toolkits.axes_grid1 import make_axes_locatable

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

pl_voi_budget.plot(ax=ax, edgecolor='0.0', linewidth=0.5, 
                  column='budget', cmap='Greens', cax=cax,
                  legend=True, 
                  legend_kwds={'label': "Mean budget per grant"})

# ax.set_aspect('equal')
ax.set_aspect(4./3)
ax.axis('off')
plt.savefig('mean_budget_map.svg', format = 'svg')


# %%
