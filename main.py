import pandas as pd
import matplotlib.pyplot as plt


#print(df.head(10)) #View first 10 data rows

#print(df.describe())

# format_dict = {'Mes':'{:%m-%Y}'} #Simplified format dictionary with values that do make sense for our data
# df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000')

#using python interactive.

df = pd.read_csv('temporal.csv')


plt.plot(df['Mes'], df['data science'], label='data science') #The parameter label is to indicate the legend. This doesn't mean that it will be shown, we'll have to use another command that I'll explain later.


plt.plot(df['Mes'], df['data science'], label='data science')
plt.plot(df['Mes'], df['machine learning'], label='machine learning')
plt.plot(df['Mes'], df['deep learning'], label='deep learning')
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity of AI terms by date')
plt.grid(True)
plt.legend()


fig, axes = plt.subplots(2,2)
axes[0, 0].hist(df['data science'])
axes[0, 1].scatter(df['Mes'], df['data science'])
axes[1, 0].plot(df['Mes'], df['machine learning'])
axes[1, 1].plot(df['Mes'], df['deep learning'])


plt.scatter(df['data science'], df['machine learning'])
plt.scatter(df['data science'], df['deep learning'])


#Bar chart

plt.bar(df['Mes'], df['machine learning'], width=20)


#Histogram

plt.hist(df['deep learning'], bins=15)