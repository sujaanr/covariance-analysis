import pandas as pd
df=pd.read_csv("/content/INF2178_A3_data.csv")
df.head(10)

# Display information on dataset
print(df.info())

# Check for NaN values
nan_count = df.isna().sum()
print(nan_count)

# Create continuous variables on General Knowledge score
df['generallknowledge'] = (df['fallgeneralknowledgescore'] + df['springgeneralknowledgescore'])/2
df['generallknowledge']

# Calculate Educational Improvement for reading, math, and general knowledge
df['Reading_Gain'] = df['springreadingscore'] - df['fallreadingscore']
df['Math_Gain'] = df['springmathscore'] - df['fallmathscore']
df['GeneralKnowledge_Gain'] = df['springgeneralknowledgescore'] - df['fallgeneralknowledgescore']
print (df['Reading_Gain'], df['Math_Gain'], df['GeneralKnowledge_Gain'] )

# Commented out IPython magic to ensure Python compatibility.
# %pip install dfply
from dfply import *
# summary statistics for dependent variable yield
summary_statistics = df >> group_by(X.incomegroup) >> summarize(n=X['generallknowledge'].count(),
                                                                mean=X['generallknowledge'].mean(),
                                                                std=X['generallknowledge'].std())
summary_statistics

import seaborn as sns
import matplotlib.pyplot as plt
fig, axs = plt.subplots(ncols=3, figsize=(18, 6))
# Scatter plot for 'fallmathscore' vs 'springmathscore' colored by 'incomegroup'
sns.scatterplot(data=df, x="fallgeneralknowledgescore", y="springgeneralknowledgescore", hue="incomegroup", palette="viridis", ax=axs[0])
# Boxplot for 'springmathscore' by 'incomegroup'
sns.boxplot(data=df, x="incomegroup", y="springgeneralknowledgescore", palette="viridis", ax=axs[1])
# Boxplot for 'totalhouseholdincome' by 'incomegroup'
sns.boxplot(data=df, x="incomegroup", y="fallgeneralknowledgescore", palette="viridis", ax=axs[2])
plt.tight_layout()
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %pip install pingouin
from pingouin import ancova
ancova_results = ancova(data=df, dv='springgeneralknowledgescore', covar='fallgeneralknowledgescore', between='incomegroup')
print(ancova_results)

import numpy as np
import pandas as pd
data = df[['incomegroup', 'fallgeneralknowledgescore', 'springgeneralknowledgescore']].copy()
print(data.head(12))

from pingouin import ancova
ancova_results = ancova(data=sample_data, dv='fallgeneralknowledgescore', covar='springgeneralknowledgescore', between='incomegroup')
print(ancova_results)

#ancova using statsmodels
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Perform the ANCOVA
model = ols('springgeneralknowledgescore ~ C(incomegroup) + fallgeneralknowledgescore', data=data).fit()
# Print the summary of the model
print(model.summary())

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Fit ANCOVA model
model = ols('springgeneralknowledgescore ~ C(incomegroup) + fallgeneralknowledgescore', data=data).fit()
# Print model summary
print(model.summary())

# Fit ANCOVA model with interaction term
model_interaction = ols('springgeneralknowledgescore ~ C(incomegroup) * fallgeneralknowledgescore', data=data).fit()
# Print model summary
print(model_interaction.summary())
