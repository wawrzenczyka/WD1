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
    data = mean_budget_by_edition)
plt.xlabel('PRELUDIUM edition')
plt.ylabel('Mean budget per grant')
plt.title('Mean grant budget over the years')
plt.savefig('mean_budget_by_edition.svg', \
    format = 'svg', bbox_inches='tight')

# %%
