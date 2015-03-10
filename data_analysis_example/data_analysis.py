import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

__author__ = 'ikatlinsky'

#Reading data from web
data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
df = pd.read_csv(data_url)

print "All data from csv:"
print df
print "\n"

print "Descriptive statistics:"
print df.describe()
print "\n"

print "Third column of data:"
print df.ix[:, 2]
print "\n"

plot.show(df.plot(kind='box'))
plot.show(sns.violinplot(df, widths=0.5, color="pastel"))
plot.show(sns.distplot(df.ix[:, 2], rug=True, bins=15))
