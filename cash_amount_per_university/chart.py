import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info_cleared.csv')

sums = df\
    .groupby(['unit'])['budget']\
    .sum()\
    .reset_index()\
    .sort_values(by = ['budget'], ascending=False)\
    .head(10)\
    .reset_index() \

sums['budget'] = sums['budget'].div(1000000)

sns.barplot(x='budget', y='unit', data=sums)
plt.ylabel('Jednostka')
plt.xlabel('Suma grantów [mln zł]')
plt.title('Jednostki o najwyższej sumie przydzielonych grantów')
plt.savefig('count_by_university.svg',format='svg', bbox_inches='tight')
