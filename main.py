import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from matplotlib import interactive

# Set the background style we want
sns.set_style('darkgrid', {"axes.edgecolor": ".15", "grid.color": ".15"})
sns.set_palette('Blues_d')

df = pd.read_csv('hotel_bookings.csv')

def summary(df):
	print(df.head())
	print(df.dtypes)
	print('Unique Values in Each Column')
	for i in df.columns:
		print(str(i) + ": " + str(len(list(df[i].unique()))))
		print('NA Values: ' + str(df[i].isna().sum()))

def set_params(ax, title, xtitle, ytitle, facecolor):
	ax.set_title(title)
	ax.set_xlabel(xtitle)
	ax.set_ylabel(ytitle)
	ax.set_facecolor(facecolor)

# Changing our Meals value into full words so they are easier to understand.
def change_meals(df, di):
	df['meal'] = df['meal'].map(di)
	return df

# Allows us to order our x axis in our charts.
Months=['January', 'February', 'March', 'April', 'May', 'June', 'July',
		'August', 'September', 'October', 'November', 'December']

# Dict to change our breakfast values.
breakfast = {'SC': 'No meal', 'BB': 'Bed & Breakfast', 'HB': 'Half Board', 'FB': 'Full Board'}

# Slicing dataframe to only look at active bookings.
# There are also two outliers where the number of babies is higher and it skews the data and makes the visuals 
# less visually appealing.
df_filter = df[(df['babies'] < 4)
	& (df['adr'] < 1000)
	& (df['adr'] > 0)
	]


# df_filter['children'] = df_filter['children'].astype('int64')

df_filter = change_meals(df=df_filter, di=breakfast)


df_country_filter = df_filter.groupby(['country', 'hotel']).mean().nlargest(20, 'adr').reset_index()

print(df_country_filter)

# Quick summary of what our data looks like
# summary(df_filter)

# Creating subplots and styling of our first figure.
fig, ax=plt.subplots(nrows=4, num='Graphical Analysis of Lead Time vs Types of People')
fig.set_facecolor("lightslategray")

# Building our four plots for figure 1.
sns.kdeplot(data=df_filter['adults'], shade=False, ax=ax[0])
sns.kdeplot(data=df_filter['children'], shade=False, ax=ax[0])
sns.kdeplot(data=df_filter['babies'], shade=False, ax=ax[0])
ax[0].legend(ncol=2, loc='upper right', framealpha=.5)

sns.barplot(x='lead_time', y='babies', data=df_filter, ax=ax[1], ci=None, orient='h', edgecolor='black')
sns.barplot(x='lead_time', y='adults', data=df_filter, ax=ax[2], ci=None, orient='h', edgecolor='black')
sns.barplot(x='lead_time', y='children', data=df_filter, ax=ax[3], ci=None, orient='h', edgecolor='black')


# Setting labels for our first plots.
set_params(ax[0], 
		title='Distribution of Number of Babies, Children, & Adults',
		xtitle='Number',
		ytitle='Occurences',
		facecolor="lightslategray")
set_params(ax[1],
		title='Number of Babies vs Lead Time of Booking',
		xtitle='Lead Time in Days',
		ytitle='Number of Babies',
		facecolor="lightslategray")
set_params(ax[2],
		title='Number of Adults vs Lead Time of Booking',
		xtitle='Lead Time in Days',
		ytitle='Number of Adults',
		facecolor="lightslategray")
set_params(ax[3],
		title='Number of Children vs Lead Time of Booking',
		xtitle='Lead Time in Days',
		ytitle='Number of Children',
		facecolor="lightslategray")


# Tight Layout prevents our labels from overlapping.
plt.tight_layout(pad=.15)
fig.show()

# Creating our Second Figure and styling it.
fig2, ax = plt.subplots(nrows=3, num='Analysis by Month')
fig2.set_facecolor('lightslategray')

# Creating our 3 subplots and styling them.
sns.barplot(x='arrival_date_month', y='adr', hue='hotel',
	data=df_filter, ci=None, ax=ax[0], edgecolor='black', order=Months)

ax[0].legend(ncol=2, loc='upper right', framealpha=.5)

sns.barplot(x='arrival_date_month', y='adr', hue='meal',
	data=df_filter, ci=None, ax=ax[1], edgecolor='black', order=Months)

ax[1].legend(ncol=2, loc='upper right', framealpha=.5)

sns.kdeplot(data=df_filter['adr'], shade=True, ax=ax[2])
ax[2].legend(framealpha=.5)

# Set labels for our charts.
set_params(ax[0],
		title='Month of Arrival vs Avg. Daily Rate by Hotel',
		xtitle='Month',
		ytitle='Avg. Daily Rate',
		facecolor='lightslategray')

set_params(ax[1],
		title='Month of Arrival vs. Avg. Daily Rate by Meal',
		xtitle='Month',
		ytitle='Avg. Daily Rate',
		facecolor='lightslategray')

set_params(ax[2],
		title='Distribution of the Avg. Daily Rate',
		xtitle='Avg. Daily Rate',
		ytitle='Occurnece',
		facecolor='lightslategray')

plt.tight_layout(pad=.15)
fig2.show()

# Creating our 3rd Subplot and styling it.
fig3, ax = plt.subplots(nrows=1,
	num='Distribution of Meal Types at Each Type of Hotel and Avg. Daily Rate')
fig3.set_facecolor('lightslategray')

sns.violinplot(x='meal', y='adr', hue='hotel', data=df_filter, ax=ax)

# Set labels for our violin plot.
set_params(ax,
		title='Distribution of Meals vs Avg. Daily Rate by Hotel',
		xtitle='Meal Type', 
		ytitle='Avg. Daily Rate',
		facecolor='lightslategray')

fig3.show()

# Fourth Figure
pal=sns.color_palette('Blues_d', len(df_country_filter))
fig4, ax=plt.subplots(nrows=1,
	num='Top 20 Most Expensive Countries by Average Daily Rate')
fig4.set_facecolor('lightslategray')

sns.barplot(x='adr', y='country', data=df_country_filter, ax=ax, ci=None, orient='h', palette=np.array(pal[:]))
set_params(ax,
		title='Top 20 Highest Average Daily Rate',
		xtitle='Price',
		ytitle='Country',
		facecolor='lightslategray')

fig4.show()


# Since we are creating two figures, in order to show them simultaneously we need to ask for an input to
# keep our program running.
input('Press "Enter" when are you done')

