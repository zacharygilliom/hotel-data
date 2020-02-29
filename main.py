import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Set the background style we want
sns.set_style('darkgrid')
sns.set_palette('Blues_d')

df = pd.read_csv('hotel_bookings.csv')

def summary(df):
	print(df.head())
	print(df.columns)
	print(df.dtypes)
	print('Unique Values in Each Column')
	for i in df.columns:
		print(str(i) + ": " + str(len(list(df[i].unique()))))

df_not_canceled = df[df['is_canceled'] == 0]

summary(df_not_canceled)

fig, ax=plt.subplots(nrows=2)
sns.barplot(x='arrival_date_month', y='stays_in_week_nights', data=df_not_canceled, hue='arrival_date_year', ci=None, ax=ax[0])
sns.kdeplot(data=df_not_canceled['adults'], shade=False, ax=ax[1])
plt.show()
