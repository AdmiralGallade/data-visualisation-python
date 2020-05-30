import pandas as pd
import matplotlib.pyplot as plt


#print(df.head(10)) #View first 10 data rows

#print(df.describe())

# format_dict = {'Mes':'{:%m-%Y}'} #Simplified format dictionary with values that do make sense for our data
# df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000')

#using python interactive.

df = pd.read_csv('temporal.csv')

plt.plot(df['Mes'], df['data science'], label='data science') #The parameter label is to indicate the legend. This doesn't mean that it will be shown, we'll have to use another command that I'll explain later.


