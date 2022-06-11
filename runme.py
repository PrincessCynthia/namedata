#!/usr/bin/env python

# To use this easy starter file:
# python -i runme.py
# >>> auto_select(fem=True,qty=10)
# 
#Or:
# >>> n=get_names_by_year_range(1980,1990)
# >>>



import pandas as pd


pd.set_option('display.max_rows', None)

def get_names_by_year_range(startyear,endyear):
    names = pd.read_csv('allyears.csv')

# Optional: Filter by year to exclude outdated info
    #names=names[names.year >= startyear]
    #names=names[names.year <= endyear]
    names=names[names.year >= startyear][names.year <= endyear]

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
    n['masc'] = n.men / (n.men + n.women)
    return n

def select_names(n,fem,min_fem=.45,max_fem=.55,min_popularity=0.9,max_popularity=1):
    m=n[n.fem>=min_fem][n.fem<=max_fem]
    if fem:
        m=m.sort_values('women')
    else:
        m=m.sort_values('men')
    l=len(m)
    maxpop=int(max_popularity*l)
    minpop=int(min_popularity*l)
    return m[minpop:maxpop]

def auto_select(fem,qty=5,startyear=1950,endyear=2020):
    if fem:
        min_fem=.9
        max_fem=1
    else:
        min_fem=0
        max_fem=.1
    n=get_names_by_year_range(startyear,endyear)
    print("Popular names")
    print(select_names(n,fem,min_fem,max_fem,.99,1).sample(qty))
    print("Semi-popular names")
    print(select_names(n,fem,min_fem,max_fem,.97,.99).sample(qty))
    print("Unusual names")
    print(select_names(n,fem,min_fem,max_fem,.7,.97).sample(qty))

