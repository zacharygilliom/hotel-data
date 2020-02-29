import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Set the background style we want
sns.set_style('darkgrid', {"axes.edgecolor": ".15", "grid.color": ".15"})
sns.set_palette('Set2')

df = pd.read_csv('hotel_bookings.csv')

def summary(df):
	print(df.head())
	print(df.columns)
	print(df.dtypes)
	print('Unique Values in Each Column')
	for i in df.columns:
		print(str(i) + ": " + str(len(list(df[i].unique()))))
		print('NA Values: ' + str(df[i].isna().sum()))

def set_params(ax, title, xtitle, ytitle):
	ax.set_title(title)
	ax.set_xlabel(xtitle)
	ax.set_ylabel(ytitle)


df_not_canceled = df[df['is_canceled'] == 0]

summary(df_not_canceled)

df['adults'] = df['adults'].astype('int32')

print(df_not_canceled['lead_time'].head(15), df_not_canceled['adults'].head(15))

fig, ax=plt.subplots(nrows=4)
sns.barplot(x='arrival_date_month', y='stays_in_week_nights', data=df_not_canceled, hue='arrival_date_year', ci=None, ax=ax[0], edgecolor='black')
sns.kdeplot(data=df_not_canceled['adults'], shade=False, ax=ax[1])
sns.kdeplot(data=df_not_canceled['children'], shade=False, ax=ax[1])
sns.barplot(x='lead_time', y='adults', data=df_not_canceled, ax=ax[2], ci=None, orient='h', edgecolor='black')
sns.barplot(x='lead_time', y='children', data=df_not_canceled, ax=ax[3], ci=None, orient='h', edgecolor='black')
fig.set_facecolor("lightslategray")
# ax[0].edgecolor = .15
ax[0].set_facecolor("lightslategray")
ax[1].set_facecolor("lightslategray")
ax[2].set_facecolor("lightslategray")
ax[3].set_facecolor("lightslategray")

set_params(ax[0], 
		title='Month of Hotel Arrival vs # of Weekdays Stayed',
		xtitle='Month of Arrival',
		ytitle='# of Weekdays')
set_params(ax[1],
		title='Distribution of Number of Children & Adults',
		xtitle='Number',
		ytitle='Kernel Distribution')
set_params(ax[2],
		title='Number of Adults vs Lead Time of Booking',
		xtitle='Lead Time in Days',
		ytitle='Number of Adults')
set_params(ax[3],
		title='Number of Children vs Lead Time of Booking',
		xtitle='Lead Time in Days',
		ytitle='Number of Children')
plt.tight_layout(pad=.15)
plt.show()

