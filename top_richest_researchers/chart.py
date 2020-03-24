import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
df = pd.read_csv(r'..\data\preludium_with_additional_info.csv')

managers_with_budget = df.groupby(['manager'])['budget'].sum().reset_index(name='budget')

managers_count = df \
    .groupby(['manager']) \
    .size() \
    .rename('count') \
    .reset_index(drop=False)

managers_all = managers_with_budget.merge(managers_count, left_on='manager', right_on='manager')

managers_all = managers_all.sort_values(by=['budget'])
managers_all.reset_index(drop=True)

best = managers_all.tail(10)
best = best.reset_index(drop=True)
best = best.sort_values(by=['budget'], ascending=False)

by_best = sns.barplot(x='manager', y='budget', data=best)
plt.xlabel('Manager')
plt.ylabel('Budget')
ax = plt.gca()
ax.set_title("Richest Scientists")
by_best.set_xticklabels(by_best.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.savefig('top_richest_researchers.svg', format='svg', bbox_inches='tight')
