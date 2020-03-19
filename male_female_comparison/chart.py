# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

preludium = pd.read_csv('../data/preludium.csv')
preludium_extra = pd.read_csv('../data/preludium_additional_info.csv')

df = preludium.merge(preludium_extra, left_on = 'id', right_on = 'Id')
df['Sex'] = np.where(df.Sex == 1, 'Male', 'Female')

# %%
df

# %%
count_by_edition = df\
    .groupby(['edition', 'Sex'])\
    .size()\
    .rename('Count')\
    .reset_index(drop = False)
budget_by_edition = df\
    .groupby(['edition', 'Sex'])\
    .mean()\
    .budget\
    .rename('MeanBudget')\
    .reset_index(drop = False)

# %%
sns.barplot(x = 'edition', y = 'Count', hue = 'Sex', \
    data = count_by_edition)
plt.xlabel('Edition')
plt.ylabel('Grant count')
plt.savefig('count_by_edition_sex.svg', \
    format = 'svg')

# %%
sns.barplot(x = 'edition', y = 'MeanBudget', hue = 'Sex', \
    data = budget_by_edition)
plt.xlabel('Edition')
plt.ylabel('Mean budget per grant')
plt.savefig('mean_budget_by_edition_sex.svg', \
    format = 'svg')

 # %%
