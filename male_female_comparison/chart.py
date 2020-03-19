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
plt.title('Grant count over the years, split by sex')
plt.savefig('count_by_edition_sex.svg', \
    format = 'svg', bbox_inches='tight')

# %%
sns.barplot(x = 'edition', y = 'MeanBudget', hue = 'Sex', \
    data = budget_by_edition)
plt.xlabel('Edition')
plt.ylabel('Mean budget per grant')
plt.title('Mean grant budget over the years, split by sex')
plt.savefig('mean_budget_by_edition_sex.svg', \
    format = 'svg', bbox_inches='tight')

# %%
df2 = df\
    .groupby(['Voivodeship', 'Sex'])\
    .mean()\
    .budget\
    .rename('Budget')\
    .reset_index(drop = False)\
    .sort_values('Budget', ascending = False)
sns.barplot(x = 'Voivodeship', y = 'Budget', \
    data = df2)
plt.xticks(rotation=90)

 # %%
