#Set month array to store months 
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#Ask user for number of years to calculate rainfall for
years = int(input('How many years: '))

years_rain = {}

for year in range(years):
    #initialize years variable
    year_rain = 0
    #initialize dictionary for each year that holds total and average
    years_rain[f'Year {year}'] = {'Total': 0, 'Average': 0}
    print(f'Year: {year}\n')
    #start monthly loop 
    for month in months:
        month_rain = int(input(f'How much rain(inches) in {month}? '))
        year_rain += month_rain
    avg = year_rain/12
    years_rain[f'Year {year}']['Total'] = year_rain
    years_rain[f'Year {year}']['Average'] = avg

total_rainfall = 0

for year_data in years_rain.values():
    total_rainfall += year_data['Total']

total_months = years * 12
total_rainfall_month_average = total_rainfall/total_months

print(years_rain)
print(f'Number of months: {total_months}')
print(f'total rainfall month average: {total_rainfall_month_average}')


#Book Points 

# Ask user for the number of books purchased
books_purchased = int(input('Enter the number of books purchased: '))

# Calculate points based on the number of books
if books_purchased == 0:
    points = 0
elif books_purchased >= 2:
    points = 5
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 8:
    points = 60

# Display the earned points
print(f'Points earned: {points}')
