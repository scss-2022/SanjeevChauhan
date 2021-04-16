import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=1000)

ax=sns.displot(data_binom,
               kde=False,
               color='blue')
ax.set(xlabel='Binomial Distribution',ylabel='frequency')
plt.show()
