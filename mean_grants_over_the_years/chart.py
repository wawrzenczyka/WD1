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

sns.barplot(x = 'edition', y = 'budget', \
    data = mean_budget_by_edition, \
    color = '#e12647')
plt.xlabel('PRELUDIUM edition')
plt.ylabel('Mean budget per grant')
title = plt.title('Mean grant budget over the years')

plt.setp(title, color='#545454')
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
