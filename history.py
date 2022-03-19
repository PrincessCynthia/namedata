#!/usr/bin/env python

# Name data downloaded from SSI at https://www.ssa.gov/oact/babynames/names.zip
# allyears.csv was generated from yob1880.txt through yob2020.txt by a hacky Linux command:
# grep .* yob*.txt | sed 's/^yob\(....\).txt:/\1,/' >allyears.csv


# This requires python 3 and pandas
# The install process for this varies based on platform but can be googled
# In Ubuntu 21.10 I just did 'sudo apt install python3-pandas'


# I've included:
#  * The original data (allyears.csv)
#  * Commands for condensing the data (FULL HISTORY section)
#  * Analyzed data, with gender ratios (ratios.csv)
#  * Instructions for quickly loading the ratios (QUICK START section)
#  * A few starter queries (SAMPLE QUERIES section)


# The easiest way to get started is to skip to the QUICK START section.



##### FULL HISTORY #####

#First, get the data into the desired format:
import pandas as pd
names = pd.read_csv('allyears.csv')

# Optional: Filter by year to exclude outdated info
names=names[names.year > 1970]

combnames=names.groupby(['name','gender'])[['qty']].sum().sort_values(['qty'])
combnames=combnames.reset_index()



m=combnames[combnames['gender'] == 'M'][['name','qty']]
f=combnames[combnames['gender'] == 'F'][['name','qty']]

m.columns=['name','men']
f.columns=['name','women']

n=pd.merge(m,f,on='name',how='outer')
n=n.fillna(0)
n.men=n.men.astype(int)
n.women=n.women.astype(int)
n['fem'] = n.women / (n.men + n.women)


# Write the data to a CSV file:
n.to_csv('ratios.csv', index=False)



##### QUICK START #####

# Load the data from a CSV file in the future:
n=pd.read_csv('ratios.csv',index_col=False)

# Note: Pandas abbreviates tables (shows top 5 and bottom 5 rows) by default
# To disable this, use:
pd.set_option('display.max_rows', None)

##### SAMPLE QUERIES #####

# Lookup a name:
n[n.name=='Jessica']

# Find names that are mostly masculine:
n[n.fem < .1].sort_values('men')

# Find all names that are 90% fem, sorted by popularity
n[n.fem > .9].sort_values('women')

# Find all names that are between 80% and 85% fem, sorted by popularity
n[n.fem > 0.80][n.fem < 0.85].sort_values('women')

# Find all names that are between 49% and 51% fem, sorted by popularity
n[n.fem > 0.49][n.fem < 0.51].sort_values('women')

# How many names are 99.9% fem and have more than 10000 women?
len(n[n.fem > 0.999][n.women > 10000])

