# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)

#plt.hist(data['Rating'])
#plt.show()

data = data[data.Rating < 6]

plt.hist(data['Rating'])
plt.show()
#Code ends here


# --------------
# code starts here
total_null = data.isna().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], axis=1, keys=['Total','Percent'])

print(missing_data)

data.dropna(inplace=True)

total_null_1 = data.isna().sum()

percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys=['Total','Percent'])

print(missing_data_1)
# code ends here


# --------------

#Code starts here
sns.catplot(x="Category", y="Rating", data=data, kind="box", height = 10)

plt.xticks(rotation=90)

plt.title('Rating vs Category [BoxPlot]')

plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
#print(data.Installs.value_counts())

data.Installs = data.Installs.str.replace('+',' ').str.replace(',','').astype('int')

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x='Installs', y='Rating', data=data)

plt.title('Rating vs Installs [RegPlot]')

plt.show()
#Code ends here


# --------------
#Code starts here
#print(data.Price.value_counts())

data.Price = data.Price.str.replace('$','').astype('float')

sns.regplot(x='Price', y='Rating', data=data)

plt.title('Rating vs Price [RegPlot]')

plt.show()
#Code ends here


# --------------

#Code starts here
print(data.Genres.unique(),'\n', '-'*50,'\n')

#for i in range(len(data.Genres)):
#    data.Genres[i] = data.Genres.iloc[i].split(';').str[0]

data.Genres = data.Genres.str.split(';').str[0]

print(data.Genres.unique(),'\n', '-'*50,'\n')

gr_mean = data[['Genres','Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe(),'\n', '-'*50,'\n')

gr_mean = gr_mean.sort_values('Rating')

print(gr_mean.head(1),'\n', '-'*50,'\n', gr_mean.tail(1))
#Code ends here


# --------------

#Code starts here
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

max_date = data['Last Updated'].max()

data['Last Updated Days'] = max_date - data['Last Updated']

data['Last Updated Days'] = data['Last Updated Days'].astype('timedelta64[D]')

sns.regplot(x='Last Updated Days', y='Rating', data=data)

plt.title('Rating vs Last Updated Days [RegPlot]')

plt.show()
#Code ends here


