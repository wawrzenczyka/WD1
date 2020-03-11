# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/preludium.csv')
df

# %%
sns.boxplot(df.edition, df.budget)

# %%
sns.boxplot(df.loc[(df.edition != 1) & (df.edition != 2), :].edition, df.budget)

# %%
plt.hist(df.edition, bins=len(np.unique(df.edition)),\
    rwidth=0.85)

# %%
count_by_edition = df.groupby(df.edition).size()\
    .reset_index(drop = False)\
    .rename(columns = { 0: 'count' })
sns.barplot(count_by_edition.edition, count_by_edition['count'])

# %%
