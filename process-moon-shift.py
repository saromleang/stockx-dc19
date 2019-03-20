#!/usr/bin/env python3

import pandas as pd
import pylunar

states_hash =  {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
  }

df = pd.read_csv('StockX-Data-Contest-2019-3.csv',parse_dates=['Order Date','Release Date'])

df['Buyer Region'].replace(states_hash,inplace = True)

years=[2017,2018,2019]
states=list(states_hash.values())
brands=['Yeezy','Off-White']

width=1500
height=1100
scl = [[0.0, 'rgb(0, 0, 0)'],[0.00000000000000000000001, 'rgb(255, 255, 255)'],[1.0, 'rgb(0, 255, 0)']]

phases=['New Moon','First Quarter','Full Moon','Last Quarter']
views=['Pairs','Total']

def translate_moon_phase(fractional_phase=None):
  length_of_lunar_cycle= 29.530587981
  if fractional_phase is None:
    return
  elif ( fractional_phase >= length_of_lunar_cycle*(0/100)  ) and ( fractional_phase < length_of_lunar_cycle*(25/100) ):
    return 'New Moon'
  elif ( fractional_phase >= length_of_lunar_cycle*(25/100) ) and ( fractional_phase < length_of_lunar_cycle*(50/100) ):
    return 'First Quarter'
  elif ( fractional_phase >= length_of_lunar_cycle*(50/100) ) and ( fractional_phase < length_of_lunar_cycle*(75/100) ):
    return 'Full Moon'
  elif ( fractional_phase >= length_of_lunar_cycle*(75/100) ):
    return 'Last Quarter'

# Detroit
mi = pylunar.MoonInfo((42, 19, 53), (-83, 2, 45))

moon_phase=[]
moon_fraction=[]

for index, row in df.iterrows():

  date_year=row['Order Date'].year
  date_month=row['Order Date'].month
  date_day=row['Order Date'].day
  mi.update((date_year, date_month, date_day, 12, 0, 0))
  fractional_phase=mi.age()
  moon_phase.append(translate_moon_phase(fractional_phase=fractional_phase))
  moon_fraction.append(fractional_phase)

df['Moon Phase']=moon_phase
df['Moon Fraction']=moon_fraction

df.to_csv("moonphase-SXDC19.csv", sep=',', encoding='utf-8')

df_refined = pd.DataFrame(columns=['Moon Phase','State','Yeezy Pairs','Off-White Pairs','Total Pairs','Yeezy Total','Off-White Total','Grand Total','Yeezy Profit','Off-White Profit','Profit Total'])

i=0
for phase in phases:
  for state in states:
    yeezy_total=0
    yeezy_pairs=0
    yeezy_profit=0
    offwhite_total=0
    offwhite_pairs=0
    offwhite_profit=0
    yeezy_total=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Yeezy')),'Sale Price'].sum()
    yeezy_profit=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Yeezy')),'Profit'].sum()
    yeezy_pairs=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Yeezy')),'Sale Price'].count()
    offwhite_total=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Off-White')),'Sale Price'].sum()
    offwhite_profit=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Off-White')),'Profit'].sum()
    offwhite_pairs=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Buyer Region'] == state) & (df['Brand'].str.endswith('Off-White')),'Sale Price'].count()
    df_refined.loc[i]=[phase,state,yeezy_pairs,offwhite_pairs,yeezy_pairs+offwhite_pairs,yeezy_total,offwhite_total,yeezy_total+offwhite_total,yeezy_profit,offwhite_profit,yeezy_profit+offwhite_profit]
    i=i+1

df_refined.to_csv("aggregate-moonphases-shift-states-SXDC19.csv", sep=',', encoding='utf-8')

df_refined_further = pd.DataFrame(columns=['Moon Phase','Yeezy Pairs','Off-White Pairs','Total Pairs','Yeezy Total','Off-White Total','Grand Total','Yeezy Profit','Off-White Profit','Profit Total'])

i=0
for phase in phases:
    yeezy_total=0
    yeezy_pairs=0
    yeezy_profit=0
    offwhite_total=0
    offwhite_pairs=0
    offwhite_profit=0
    yeezy_total=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Yeezy')),'Sale Price'].sum()
    yeezy_profit=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Yeezy')),'Profit'].sum()
    yeezy_pairs=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Yeezy')),'Sale Price'].count()
    offwhite_total=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Off-White')),'Sale Price'].sum()
    offwhite_profit=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Off-White')),'Profit'].sum()
    offwhite_pairs=df.loc[(df['Moon Phase'].str.endswith(phase)) & (df['Brand'].str.endswith('Off-White')),'Sale Price'].count()
    df_refined_further.loc[i]=[phase,yeezy_pairs,offwhite_pairs,yeezy_pairs+offwhite_pairs,yeezy_total,offwhite_total,yeezy_total+offwhite_total,yeezy_profit,offwhite_profit,yeezy_profit+offwhite_profit]
    i=i+1

df_refined_further.to_csv("aggregate-moonphases-shift-SXDC19.csv", sep=',', encoding='utf-8')

