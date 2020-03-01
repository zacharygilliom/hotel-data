import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from matplotlib import interactive

# Set the background style we want
sns.set_style('darkgrid', {"axes.edgecolor": ".15", "grid.color": ".15"})
sns.set_palette('Set2')

df = pd.read_csv('hotel_bookings.csv')

print(df[df['babies'] > 3].head())

def summary(df):
	print(df.head())
	print(df.columns)
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

# Slicing dataframe to only look at active bookings.
# There are also two outliers where the number of babies is higher and it skews the data and makes the visuals 
# less visually appealing.
df_not_canceled = df[(df['is_canceled'] == 0) & (df['babies'] < 4)]

# Quick summary of what our data looks like
summary(df_not_canceled)

# Creating subplots and styling figure.
fig, ax=plt.subplots(nrows=4, num='Graphical Analysis of Lead Time vs Types of People')
fig.set_facecolor("lightslategray")

# Building our Four Plots.
sns.kdeplot(data=df_not_canceled['adults'], shade=False, ax=ax[0])
sns.kdeplot(data=df_not_canceled['children'], shade=False, ax=ax[0])
sns.kdeplot(data=df_not_canceled['babies'], shade=False, ax=ax[0])

sns.barplot(x='lead_time', y='babies', data=df_not_canceled, ax=ax[1], ci=None, orient='h', edgecolor='black')
sns.barplot(x='lead_time', y='adults', data=df_not_canceled, ax=ax[2], ci=None, orient='h', edgecolor='black')
sns.barplot(x='lead_time', y='children', data=df_not_canceled, ax=ax[3], ci=None, orient='h', edgecolor='black')


# Setting labels for our plots.
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

ax[0].legend(ncol=2, loc='upper right',framealpha=.5)

# Tight Layout prevents our labels from overlapping.
plt.tight_layout(pad=.15)
fig.show()

# Creating our Second Figure and styling it.
fig2, ax = plt.subplots(nrows=1)
fig2 = plt.figure(2)
fig2.set_facecolor('lightslategray')

# Creating our subplots.
sns.barplot(x='adults', y='lead_time', data=df_not_canceled, ci=None, ax=ax, edgecolor='black')
ax.set_facecolor('lightslategray')

fig2.show()

# Since we are creating two figures, in order to show them simultaneously we need to ask for an input to
# keep our program running.
input('Press "Enter" when are you done')
# plt.show()

