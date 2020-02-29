import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Set the background style we want
sns.set_style('darkgrid')
sns.set_palette(sns.cubehelix_palette())

df = pd.read_csv('hotel_bookings.csv')

def summary(df):
	print(df.head())
	print(df.columns)
	print(df.dtypes)
	print('Unique Values in Each Column')
	for i in df.columns:
		print(str(i) + ": " + str(len(list(df[i].unique()))))
		print('NA Values: ' + str(df[i].isna().sum()))

df_not_canceled = df[df['is_canceled'] == 0]

summary(df_not_canceled)

df['adults'] = df['adults'].astype('int32')

print(df_not_canceled['lead_time'].head(15), df_not_canceled['adults'].head(15))

fig, ax=plt.subplots(nrows=4)
sns.barplot(x='arrival_date_month', y='stays_in_week_nights', data=df_not_canceled, hue='arrival_date_year', ci=None, ax=ax[0])
sns.kdeplot(data=df_not_canceled['adults'], shade=False, ax=ax[1])
sns.kdeplot(data=df_not_canceled['children'], shade=False, ax=ax[1])
sns.barplot(x='lead_time', y='adults', data=df_not_canceled, ax=ax[2], ci=None, orient='h')
sns.barplot(x='lead_time', y='children', data=df_not_canceled, ax=ax[3], ci=None, orient='h')
fig.set_facecolor("slategray")
ax[0].set_facecolor("lightslategray")
ax[1].set_facecolor("lightslategray")
ax[2].set_facecolor("lightslategray")
ax[3].set_facecolor("lightslategray")
# ax[1].set_axis_bgcolor("lightslategray")
# ax[2].set_axis_bgcolor("lightslategray")
# ax[3].set_axis_bgcolor("lightslategray")
plt.show()

