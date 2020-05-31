import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from bokeh.plotting import figure, output_file, save
output_file('data_science_popularity.html')

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


#Marked Data

plt.plot(df['Mes'], df['data science'], label='data science')
plt.plot(df['Mes'], df['machine learning'], label='machine learning')
plt.plot(df['Mes'], df['deep learning'], label='deep learning')
plt.xlabel('Date')
plt.ylabel('Popularity')
plt.title('Popularity of AI terms by date')
plt.grid(True)
plt.text(x='data_x', y=80, s=r'lambda=Value r^2=to_be_calc') #Coordinates use the same units as the graph
plt.annotate('A red arrow', xy=('2014-01-01', 30), xytext=('2006-01-01', 50), arrowprops={'facecolor':'red', 'shrink':0.05})




#Seaborne

sns.set()
sns.scatterplot(df['Mes'], df['data science'])

#Heatmap

sns.heatmap(df.corr(), annot=True, fmt='.2f')

#Pair plot
sns.pairplot(df)

sns.pairplot(df, hue='categorical')

sns.jointplot(x='data science', y='machine learning', data=df)

#violin..plot?

sns.catplot(x='categorical', y='data science', kind='violin', data=df)


#bokeh

p = figure(title='data science', x_axis_label='Mes', y_axis_label='data science')
p.line(df['Mes'], df['data science'], legend='popularity', line_width=2)
save(p)