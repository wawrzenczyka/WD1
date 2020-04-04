# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

preludium = pd.read_csv('../data/preludium_with_additional_info_cleared.csv')

# %%
mean_budget_by_edition = preludium\
    .groupby(preludium.edition)\
    .mean()\
    .reset_index(drop = False)\
    .loc[:, ['edition', 'budget']]

mean_budget_by_edition['budget'] = \
    mean_budget_by_edition.budget / 1000

sns.barplot(x = 'edition', y = 'budget', \
    data = mean_budget_by_edition, \
    color = '#e12647')
plt.xlabel('Edycja PRELUDIUM')
plt.ylabel('Średnia wysokość grantu (tys. zł)')
# title = plt.title('Mean grant budget over the years')

# plt.setp(title, color='#545454')
ax = plt.gca()
# ax.spines['bottom'].set_color('#545454')
# ax.spines['top'].set_color('#545454')
# ax.spines['left'].set_color('#545454')
# ax.spines['right'].set_color('#545454')
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.xaxis.label.set_color('#545454')
ax.yaxis.label.set_color('#545454')
ax.tick_params(axis='x', colors='#545454')
ax.tick_params(axis='y', colors='#545454')

plt.savefig('mean_budget_by_edition.svg', \
    format = 'svg', bbox_inches='tight', \
    transparent = True)
plt.savefig('mean_budget_by_edition.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
mean_budget_by_edition = preludium\
    .groupby(preludium.edition)\
    .mean()\
    .reset_index(drop = False)\
    .loc[:, ['edition', 'budget']]

mean_budget_by_edition['budget'] = \
    mean_budget_by_edition.budget / 1000

sns.barplot(x = 'edition', y = 'budget', \
    data = mean_budget_by_edition, \
    color = '#e12647')
plt.xlabel('Edycja PRELUDIUM')
plt.ylabel('Średnia wysokość grantu (tys. zł)')
# title = plt.title('Mean grant budget over the years')

ax = plt.gca()
ax.spines['bottom'].set_color('gray')
sns.despine(left = True, top = True, right = True)
ax.tick_params(axis='both', which='both', length=0)

ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='solid')

plt.savefig('mean_budget_by_edition_v2.svg', \
    format = 'svg', bbox_inches='tight', \
    transparent = True)
plt.savefig('mean_budget_by_edition_v2.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
mean_budget_by_edition = preludium\
    .groupby(preludium.edition)\
    .mean()\
    .reset_index(drop = False)\
    .loc[:, ['edition', 'budget']]

mean_budget_by_edition['budget'] = \
    mean_budget_by_edition.budget / 1000

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

# -------------

budgets = pd.read_csv('../data/budgets.csv')
budgets['id'] = pd.to_numeric(budgets['name'].str[9:])
budgets = budgets.drop(columns=['name'])
budgets.head()

sns.barplot(x = 'id', y = 'budget', \
    data = budgets, \
    color = '#e12647', ax = ax1)
ax1.set_xlabel('Edycja PRELUDIUM')
ax1.set_ylabel('Budżet konkursu (mln zł)')
# title = plt.title('Mean grant budget over the years')

ax1.spines['bottom'].set_color('gray')
sns.despine(ax = ax1, \
    left = True, top = True, right = True)
ax1.tick_params(axis='both', which='both', length=0)

ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='solid')

# -------------

sns.barplot(x = 'edition', y = 'budget', \
    data = mean_budget_by_edition, \
    color = '#e12647', ax = ax2)
ax2.set_xlabel('Edycja PRELUDIUM')
ax2.set_ylabel('Średnia wysokość grantu (tys. zł)')
# title = plt.title('Mean grant budget over the years')

ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

ax2.spines['bottom'].set_color('gray')
sns.despine(ax = ax2, \
    left = True, top = True, right = True)
ax2.tick_params(axis='both', which='both', length=0)

ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='solid')

plt.savefig('budgets_grants_combined.svg', \
    format = 'svg', bbox_inches='tight', \
    transparent = True)
plt.savefig('budgets_grants_combined.png', \
    format = 'png', bbox_inches='tight', \
    transparent = True, dpi = 300)

# %%
