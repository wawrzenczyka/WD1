# %%
import numpy as np
import pandas as pd

df = pd.read_csv('data/grants_larger.csv')

# %%
df['type2'] = df.type.str.replace('Konkurs: ', '').str.replace(r'  - ogłoszony .*', '')

# %%
np.unique(df.type2)

# %%
df['type3'] = df.type2.str.replace(r' [0-9]+', '')

# %%
np.unique(df.type3)

# %%
df['edition'] = df.type2.str.replace(r'[A-Z]+ *', '')

# %%
np.unique(df.edition)

# %%
df['subpanel_code'] = df.subpanel.str.extract(r'([A-Z]{2}[0-9]+)')[0]

# %%
np.unique(df.subpanel_code)

# %%
df['budget_numeric'] = pd.to_numeric(\
    df.budget.str.replace(r'Przyznana kwota: ', '')\
        .str.replace(r' PLN', '')\
        .str.replace(r' ', '')\
)

# %%
df['duration_numeric'] = df.duration.str.extract(r'([0-9]+)')

# %%
df['coinvestigators_numeric'] = df.coinvestigators.str.extract(r'([0-9]+)')

# %%
df = df.loc[:, ['type3', 'edition', 'subpanel_code', \
        'budget_numeric', 'duration_numeric', 'coinvestigators_numeric']]\
    .rename(columns={ "type3": "type" })
df

# %%
preludium_df = df.loc[df.type == 'PRELUDIUM', :]\
    .reset_index(drop = True)

# %%
preludium_df.to_csv('data/preludium.csv')

# %%
