# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:49:37 2018

@author: Levi
"""

import pandas as pd 

# Code currently takes a long time to run
# It is parsing through over 500,000 crimes
# Need to see if we can get it to run faster

# Just need to save csv file in same folder as py file
crime_report = pd.read_csv('crime.csv')
size = len(crime_report)

#athmar_park = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])
#
#auraria = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 
#
#baker = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 
#
#barnum = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])  
#
#barnum_west = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])  
#
#bear_valley = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
#       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
#       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
#       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
#       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 

lincoln_park = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 

neighborhood_id = crime_report.iloc[:,16]
for i in range(size):
#    if neighborhood_id[i] == 'athmar-park':
#        athmar_park = athmar_park.append(crime_report.loc[i,:], ignore_index = True)
#        
#    elif neighborhood_id[i] == 'auraria':
#        auraria = auraria.append(crime_report.loc[i,:], ignore_index = True)
#        
#    elif neighborhood_id[i] == 'baker':
#        baker = baker.append(crime_report.loc[i,:], ignore_index = True)
#    
#    elif neighborhood_id[i] == 'barnum':
#        barnum = barnum.append(crime_report.loc[i,:], ignore_index = True)
#        
#    elif neighborhood_id[i] == 'barnum-west':
#        barnum_west = barnum_west.append(crime_report.loc[i,:], ignore_index = True)
#        
#    elif neighborhood_id[i] == 'bear-valley':
#        bear_valley = bear_valley.append(crime_report.loc[i,:], ignore_index = True) 
        
    if neighborhood_id[i] == 'lincoln-park':
        lincoln_park = lincoln_park.append(crime_report.loc[i,:], ignore_index = True) 
        
        
        
#athmar_park.to_csv('Neighborhood Files/athmar_park.csv')
#auraria.to_csv('Neighborhood Files/auraria.csv')
#baker.to_csv('Neighborhood Files/baker.csv')
#barnum.to_csv('Neighborhood Files/barnum.csv')
#barnum_west.to_csv('Neighborhood Files/barnum_west.csv')
#bear_valley.to_csv('Neighborhood Files/bear_valley.csv')
lincoln_park.to_csv('Neighborhood Files/lincoln_park.csv')