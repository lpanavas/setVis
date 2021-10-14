import pandas as pd
import seaborn as sns
sns.set_theme(color_codes=True)
iris = sns.load_dataset("iris")
species = iris.pop("species")


d = {'subject1': [0, 0, 0, 0, 0, 1], 'subject2': [0, 0, 0, 1, 0, 1], 'subject3': [0, 0, 0, 1, 1, 1],
     'subject4': [1, 0, 0, 1, 1, 0], 'subject5': [1, 0, 0, 1, 0, 0], 'subject6': [0, 0, 0, 1, 0, 0],
     'subject7': [0, 0, 0, 0, 1, 0], 'subject8': [0, 0, 1, 0, 1, 0], 'subject9': [0, 0, 1, 0, 0, 0], 'subject10': [1, 1, 0, 0, 0, 0]}
df = pd.DataFrame(data=d)
g = sns.clustermap(df)
