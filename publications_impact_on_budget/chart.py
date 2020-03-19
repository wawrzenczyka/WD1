# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/preludium_with_additional_info.csv')
df['sex'] = np.where(df.sex == 1, 'Male', 'Female')

# %%
df = df\
    .assign(publications = df['magazines publications'] \
        + df['book publications'] \
        + df['post-conference publications'])

# %%
df.publications.unique()

# %%
sns.scatterplot(x = 'publications', y = 'budget', \
    data = df)
plt.savefig('scatterplot.svg', \
    format = 'svg', bbox_inches='tight')

# %%
sns.boxplot(x = 'publications', y = 'budget', \
    data = df)
plt.savefig('boxplot.svg', \
    format = 'svg', bbox_inches='tight')

# %%
sns.barplot(x = 'publications', y = 'budget', \
    data = df)
plt.savefig('barplot.svg', \
    format = 'svg', bbox_inches='tight')

# %%
