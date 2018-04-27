import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', encoding="cp936")
df = df.dropna()

plt.figure()
df.plot(x=df['date'])
plt.savefig('first.png')

plt.figure()
df1 = df[:]
df1['month'] = df['date'].map(lambda x: x[:x.rindex('-')])
df1 = df1.groupby(by='month', as_index=False).sum()
df1.plot(x=df1['month'], kind='bar')
plt.savefig('second.png')

plt.figure()
df2 = df1.drop('month', axis = 1).diff()
m = df2['count'].nlargest(2).keys()[1]
with open('maxMonth.txt', 'w') as fp:
    fp.write(df1.loc[m, 'month'])

plt.figure()
one = df1[:3]['count'].sum()
two = df1[3:6]['count'].sum()
three = df1[6:9]['count'].sum()
four = df1[9:12]['count'].sum()
plt.pie([one, two, three, four], labels = ['one', 'two', 'three', 'four'])
plt.savefig('third.png')

