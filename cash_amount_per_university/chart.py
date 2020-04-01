import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info_cleared.csv')

sums = df \
    .groupby(['unit'])['budget'] \
    .sum() \
    .reset_index() \
    .sort_values(by=['budget'], ascending=False) \
    .head(10) \
    .reset_index()

sums['budget'] = sums['budget'].div(1000000)
sns.set_style("whitegrid")
sns.barplot(x='budget', y='unit', data=sums, color='#e12647')
plt.ylabel('Jednostka')
plt.xlabel('Suma grantów [mln zł]')

# title = 'Jednostki o najwyższej sumie przydzielonych grantów'
# plt.setp(title, color='#545454')

ax = plt.gca()
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.xaxis.label.set_color('#545454')
ax.yaxis.label.set_color('#545454')
ax.tick_params(axis='x', colors='#545454')
ax.tick_params(axis='y', colors='#545454')

plt.savefig('count_by_university.svg', format='svg', bbox_inches='tight', transparent=True)
plt.savefig('count_by_university.png', format='png', bbox_inches='tight', transparent=True, dpi=800)
