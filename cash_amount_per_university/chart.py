import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info_cleared.csv')
#
# managers_count = df \
#     .groupby(['unit']) \
#     .sum() \
#     .reset_index(drop=False)
#
# print(managers_count)

sums = df\
    .groupby(['unit'])['budget']\
    .sum()\
    .reset_index()\
    .sort_values(by = ['budget'], ascending=False)\
    .head(10)\
    .reset_index()
print(sums)
# %%
sns.barplot(x='unit', y='budget', data=sums)
plt.xlabel('Jednostka')
plt.ylabel('Suma grantów')
plt.title('Jednostki o najwyższej sumie przydzielonych grantów')
plt.savefig('count_by_university.svg',format='svg', bbox_inches='tight')
