#calculate Yoy percent change
def calculate_yoy(element, prev_year_trips):
    if element['year'] - 1 in prev_year_trips:
        prev_year_trips = prev_year_trips[element['year'] - 1]
        return{
            'year': element['year'],
            "total trips per year": element['total trips per year'],
            'YoY percent change': ((element['total trips per year'] - prev_year_trips) / prev_year_trips) * 100
        }
    else:
        return{
            'year': element['year'],
            "total trips per year": element['total trips per year'],
            'YoY percent change': None
        }
    