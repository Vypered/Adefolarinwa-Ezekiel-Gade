#defining Nigerian season and time of day buckets
#NOTE: TO SUCCESSFULLY UTILIZE THE CALCULATOR FOR BI ANALYSIS, INSTALL PYTHON APACHE-BEAM LIBRARY.
def get_season(month):
    if month in [11,12,1,2,3,4]: return 'Dry Season'
    else: return 'Rainy Season'


def get_time_of_day(hour):
    if hour >= 19: return 'Night'
    elif hour >= 5: return 'Morning'
    elif hour >= 12: return 'Afternoon'
    else: return 'Evening'

#Transfrom your data
peak_usage = userdata | beam.Map(lambda x: {
    'season': get_season(x['month']),
    'time_of_day': get_time_of_day(x['hour']),
    'weather' : x['weather'],
    'trip count' : x['trip count'],
})
