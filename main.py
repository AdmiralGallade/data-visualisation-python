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

output_file('multiple_graphs.html')
s1 = figure(width=250, plot_height=250, title='data science')
s1.circle(df['Mes'], df['data science'], size=10, color='navy', alpha=0.5)
s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range, title='machine learning') #share both axis range
s2.triangle(df['Mes'], df['machine learning'], size=10, color='red', alpha=0.5)
s3 = figure(width=250, height=250, x_range=s1.x_range, title='deep learning') #share only one axis range
s3.square(df['Mes'], df['deep learning'], size=5, color='green', alpha=0.5)
p = gridplot([[s1, s2, s3]])
save(p)




#folium


import folium
m1 = folium.Map(location=[41.38, 2.17], tiles='openstreetmap', zoom_start=18)
m1.save('map1.html')


m2 = folium.Map(location=[41.38, 2.17], tiles='openstreetmap', zoom_start=16)
folium.Marker([41.38, 2.176], popup='<i>You can use whatever HTML code you want</i>', tooltip='click here').add_to(m2)
folium.Marker([41.38, 2.174], popup='<b>You can use whatever HTML code you want</b>', tooltip='dont click here').add_to(m2)
m2.save('map2.html')






