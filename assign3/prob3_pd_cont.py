
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

data_normal = norm.rvs(size=10000,loc=0,scale=1)

ax=sns.displot(data_normal,
               bins=100,
               kde=True)

ax.set(xlabel='Frequency Distribution',ylabel='frequency')
plt.show()
