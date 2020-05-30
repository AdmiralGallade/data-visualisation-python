import pandas as pd
df = pd.read_csv('temporal.csv')


#print(df.head(10)) #View first 10 data rows

#print(df.describe())


format_dict = {'data science':'${0:,.2f}', 'Mes':'{:%m-%Y}', 'machine learning':'{:.2%}'}
#We make sure that the Month column has datetime format
df['Mes'] = pd.to_datetime(df['Mes'])
#We apply the style to the visualization
print(df.head().style.format(format_dict))