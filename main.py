import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('hotel_bookings.csv')

print(df.head())
print(df.columns)

# for i in df.columns:
# 	print('Columns Name: ' + str(i).upper())	
# 	print(df[i].unique())
# 	print('\n')
df_not_canceled = df[df['is_canceled'] == 0]
print(df_not_canceled['is_canceled'])
print(df_not_canceled.shape)

sns.barplot(x='arrival_date_month', y='stays_in_week_nights', data=df_not_canceled, hue='arrival_date_year')
plt.show()
