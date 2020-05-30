import pandas as pd
df = pd.read_csv('temporal.csv')


#print(df.head(10)) #View first 10 data rows

#print(df.describe())

format_dict = {'Mes':'{:%m-%Y}'} #Simplified format dictionary with values that do make sense for our data
df.head().style.format(format_dict).highlight_max(color='darkgreen').highlight_min(color='#ff0000')