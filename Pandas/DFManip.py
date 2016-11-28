import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import re

aliments = pd.read_csv('aliments.csv', delimiter='\t')
ind = aliments['packaging'].value_counts() > 30

# x = pd.cut(aliments[u'sugars_100g'].dropna(), 5, labels=['a', 'b', 'c', 'd', 'e'])
# print(x)
y, out = pd.qcut(aliments[u'sugars_100g'].dropna(), 5, labels=['a', 'b', 'c', 'd', 'e'], retbins=True)
print(out)

'''
csv = ' John,     47 rue Barrault, 36 ans  '
credits_cards = ' Thanks for paying with 1098-1203-1233-2354        '
cred = re.compile(r'\d{4}-\d{4}')

# print(csv.replace('John', 'Fares'))
email = """
Voici le fichier complété et le calendrier et la liste des adresses des élèves (elles ne seront opérationnelles que la semaine prochaine).
pierre.arbelet@telECOM-Paristech.fr francois.bLAS@TElecom-parisTECH.fr geoffray.bories@telecom-paristech.fr claire.chazelas@TELECOM-PAristech.fr dutertre@telecom-paristech.fr nde.fOKOU@telecom-paristech.fr wei.he@telecom-paristech.fr anthony.hayot@telecom-paristech.fr frederic.hohner@telecom-paristech.fr yoann.janvier@telecom-paristech.fr mimoune.louarradi@telecom-paristech.fr david.luz@telecom-paristech.fr nicolas.marsallon@telecom-paristech.fr paul.mochkovitch@telecom-paristech.fr martin.prillard@telecom-paristech.fr christian.penon@telecom-paristech.fr gperrin@telecom-paristech.fr anthony.reinette@telecom-paristech.fr florian.riche@telecom-paristech.fr romain.savidan@telecom-paristech.fr yse.wanono@telecom-paristech.fr ismail.arkhouch@telecom-paristech.fr philippe.cayeux@telecom-paristech.fr hicham.hallak@telecom-paristech.fr arthur.dupont@telecom-paristech.fr dabale.kassim@telecom-paristech.fr xavier.lioneton@telecom-paristech.fr sarra.mouas@telecom-paristech.fr jonathan.ohayon@telecom-paristech.fr alix.saas-monier@telecom-paristech.fr thabet.chelligue@telecom-paristech.fr amoussou@telecom-paristech.fr pierre.arbelet@telecom-paristech.fr
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex_email = re.compile(pattern, flags=re.IGNORECASE)
extracts = regex_email.findall(email)

# Find groups in each string (return Series/ DataFrame in case multiple groups)
df = Series(extracts).str.upper().str.extract('([A-Z0-9_%+-]+)\.?([A-Z0-9_%+-]*)@([A-Z0-9.-]+)\.([A-Z]{2,4})')

df = df.rename(columns = {0:'firstname', 1:'lastname', 2:'ecole',3:'domain'} )

df.index = df.index.map(lambda x: 'Eleve ' +str(x))

print(df)

### PART 0
aliments = pd.read_csv('aliments.csv', delimiter='\t')
aliments = aliments.set_index('product_name')
# print(aliments.dropna(subset=['traces'])['traces'].str.split(',', expand=True))
# print(aliments.dropna(axis=0, how='all'))
# print(aliments.dropna(subset=['traces'])['traces'].str.split(',', expand=True))
# aliments_with_traces = aliments.dropna(subset=['traces'])
# x = aliments_with_traces['traces']
# print(x)
# traces_iter = (set(x.split(',')) for x in aliments_with_traces['traces'])  # sans reptition
# print(x.str.split(','))
# traces = set.union(*traces_iter)
# print(traces_iter)
# haha = (x for x in range(10))
# print(haha)

aliments_with_traces = aliments.dropna(subset=['traces'])

traces_iter = (set(x.split(',')) for x in aliments_with_traces['traces'])
traces = set.union(*traces_iter)

dummies = pd.DataFrame(np.zeros((len(aliments_with_traces), len(traces))), columns=traces)

print(traces)
for i, tr in enumerate(aliments_with_traces.traces):
     dummies.ix[i, tr.split(',')] = 1

print(dummies)

### Lesson 5 - PART 1
cameras = pd.read_csv("Camera.csv", delimiter=";", skiprows=[1])  # Separator in csv file ;
# Rows selection in DataFrame
# df = df.ix[1:]  # iloc/ix, alternative solution: skip_rows = [1]
# print("Number of lines and columns: {}".format(cameras.shape))
# print("Column names: {}".format(cameras.columns))
# Index setting
# cameras_clean = cameras.set_index("Model").astype(float)
# Renaming of columns
cameras_clean = cameras.rename(columns={"Weight (inc. batteries)": "Weight"})
brand = cameras_clean['Model'].apply(lambda x: x.split(' ')[0])
cameras_clean['Brand'] = brand
# Average weight of each brand
# cameras_clean.groupby('Brand')['Weight'].mean()
# cameras_clean.groupby('Brand')['Price'].mean()  # Pandas Series returned (index: Price)
x = cameras_clean.groupby('Brand').agg({'Weight': np.mean, 'Price': np.mean})
print(x.sort_values(['Weight'], ascending=False)[:5])


# print(cameras_clean.groupby('Brand')['Max resolution', 'Low resolution', 'Effective pixels'].sum())

#brand = cameras_clean.index.map(lambda x: x.split(' ')[0])
#cameras_clean = cameras_clean.set_index(brand)

# cameras_clean['brand'] = brand

### Lesson 5 - PART 2
# List of lists
releves = [
         ['lundi','temperature',28]
         ,['lundi','ensoleillement',4]
         ,['lundi','pollution',5]
         ,['lundi','pluie',100]
         ,['mardi','temperature',28]
         ,['mardi','ensoleillement',4]
         ,['mardi','pollution',5]
         ,['mardi','pluie',100]
         ,['mercredi','temperature',28]
         ,['mercredi','ensoleillement',4]
         ,['mercredi','pollution',5]
         ,['mercredi','pluie',100]
         ,['jeudi','temperature',28]
         ,['jeudi','ensoleillement',4]
         ,['jeudi','pollution',5]
         ,['jeudi','pluie',100]
         ,['vendredi','temperature',28]
         ,['vendredi','ensoleillement',4]
         ,['vendredi','pollution',5]
         ,['vendredi','pluie',100]
         ]
#PIVOT
releves = [
          ['lundi','temperature',28]
         ,['lundi','ensoleillement',4]
         ,['lundi','pollution',5]
         ,['lundi','pluie',100]
         ,['mardi','temperature',28]
         ,['mardi','ensoleillement',4]
         ,['mardi','pollution',5]
         ,['mardi','pluie',100]
         ,['mercredi','temperature',28]
         ,['mercredi','ensoleillement',4]
         ,['mercredi','pollution',5]
         ,['mercredi','pluie',100]
         ,['jeudi','temperature',28]
         ,['jeudi','ensoleillement',4]
         ,['jeudi','pollution',5]
         ,['jeudi','pluie',100]
         ,['vendredi','temperature',28]
         ,['vendredi','ensoleillement',4]
         ,['vendredi','pollution',5]
         ,['vendredi','pluie',100]
         ]

cities_data = pd.DataFrame(releves, columns=['day', 'observation', 'value'])
print(cities_data)
cities_data_wide = cities_data.pivot('day','observation','value')
print(cities_data_wide)
cities_data_wide = cities_data.pivot('day','observation','value').reset_index()
print(cities_data_wide)
observations =[ u'ensoleillement', u'pluie', u'pollution', u'temperature']
print(pd.melt(cities_data_wide, id_vars=['day'], value_vars=observations))
'''
# Series.value counts: returns object containing counts of unique values.