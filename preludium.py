# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

preludium = pd.read_csv('data/preludium.csv')
preludium

# %%
sns.boxplot(preludium.edition, preludium.budget)
plt.show()

# %%
sns.boxplot(preludium.loc[(preludium.edition != 1) & (preludium.edition != 2), :].edition, preludium.budget)
plt.show()

# %%
plt.hist(preludium.edition, bins=len(np.unique(preludium.edition)),\
    rwidth=0.85)
plt.show()

# %%
count_by_edition = preludium.groupby(preludium.edition).size()\
    .reset_index(drop = False)\
    .rename(columns = { 0: 'count' })
sns.barplot(count_by_edition.edition, count_by_edition['count'])
plt.show()

# %%
