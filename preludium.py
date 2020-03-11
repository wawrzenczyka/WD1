# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/preludium.csv')
df

# %%
plt.hist(df.edition, bins=len(np.unique(df.edition)),\
    rwidth=0.85)

# %%
