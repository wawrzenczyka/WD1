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
count_by_sex = df\
    .groupby(['Sex'])\
    .size()\
    .rename('Count')\
    .reset_index(drop = False)
count_by_sex['Sex'] = \
    np.where(count_by_sex['Sex'] == 'Male', \
        'Mężczyźni', \
        'Kobiety')
plt.title('Liczba przyznanych grantów')

import matplotlib.pyplot as plt
plt.pie(count_by_sex.Count, labels=count_by_sex.Sex, \
    startangle = -40, explode = [0.1, 0], \
    autopct='%1.0f%%', colors = ['#E12647', '#798897'], \
    shadow=True)

plt.savefig('count_by_sex_pie.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
budget_by_sex = df\
    .groupby(['Sex'])\
    .mean()\
    .budget\
    .rename('MeanBudget')\
    .reset_index(drop = False)
budget_by_sex['Sex'] = \
    np.where(budget_by_sex['Sex'] == 'Male', \
        'Mężczyźni', \
        'Kobiety')

import matplotlib.pyplot as plt
plt.pie(budget_by_sex.MeanBudget, labels=budget_by_sex.Sex, \
    startangle = -40, explode = [0.1, 0], \
    autopct='%1.0f%%', colors = ['#E12647', '#798897'], \
    shadow=True)

plt.title('Średnia wysokość grantu')

plt.savefig('budget_by_sex_pie.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
budget_by_sex = df\
    .groupby(['Sex'])\
    .mean()\
    .budget\
    .rename('MeanBudget')\
    .reset_index(drop = False)
budget_by_sex['Sex'] = \
    np.where(budget_by_sex['Sex'] == 'Male', \
        'Mężczyźni', \
        'Kobiety')

import matplotlib.pyplot as plt

sns.barplot(x = 'Sex', y = 'MeanBudget', \
    palette = ['#E12647', '#798897'], \
    data = budget_by_sex)

plt.xlabel('Płeć')
plt.ylabel('Średnia wysokość grantu (zł)')

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('budget_by_sex_bar.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
budget_by_sex = df\
    .groupby(['Sex'])\
    .mean()\
    .budget\
    .rename('MeanBudget')\
    .reset_index(drop = False)
budget_by_sex['Sex'] = \
    np.where(budget_by_sex['Sex'] == 'Male', \
        'Mężczyźni', \
        'Kobiety')

budget_by_sex['MeanBudget'] = \
    budget_by_sex['MeanBudget'] / 1000

import matplotlib.pyplot as plt
sns.set_style("whitegrid")
sns.barplot(x = 'Sex', y = 'MeanBudget', \
    palette = ['#E12647', '#798897'], \
    data = budget_by_sex)

plt.xlabel('Płeć')
plt.ylabel('Średnia wysokość grantu (tys. zł)')

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ax.set_axisbelow(True)
# ax.yaxis.grid(color='gray', linestyle='dashed')

plt.savefig('budget_by_sex_bar_v2.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
budget_by_sex = df\
    .groupby(['Sex'])\
    .mean()\
    .budget\
    .rename('MeanBudget')\
    .reset_index(drop = False)
budget_by_sex['Sex'] = \
    np.where(budget_by_sex['Sex'] == 'Male', \
        'Mężczyźni', \
        'Kobiety')

budget_by_sex['MeanBudget'] = \
    budget_by_sex['MeanBudget'] / 1000

import matplotlib.pyplot as plt
sns.reset_defaults()
# sns.set_style("whitegrid")
sns.barplot(x = 'Sex', y = 'MeanBudget', \
    palette = ['#E12647', '#798897'], \
    data = budget_by_sex)

plt.xlabel('Płeć')
plt.ylabel('Średnia wysokość grantu (tys. zł)')

ax = plt.gca()
ax.spines['bottom'].set_color('gray')
sns.despine(left = True, top = True, right = True)
ax.tick_params(axis='both', which='both', length=0)

ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='solid')

plt.savefig('budget_by_sex_bar_v3.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
