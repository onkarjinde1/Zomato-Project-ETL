# Python program to convert
# JSON file to CSV
  
  
import json
import csv
from datetime import datetime

with open('D:/ll/file1.json',) as json_file:
    zomato_data = json.load(json_file)
    #data = json.load(json_file)
    restaurants_data = zomato_data[0]
    print(restaurants_data)
file1_data = restaurants_data['restaurants']

# dd/mm/YY
csv_file_name = 'D:/zomato_'
now = datetime.now()
date1 = now.strftime("%Y-%m-%d")
# now we will open a file for writing
zomato_csv = open(csv_file_name + date1 + '.csv','w')
  
# create the csv writer object
csv_writer = csv.writer(zomato_csv) 
# headers to the CSV file

#def new_func(header):

    #csv.writer.writerow(header)

header = ['Restaurant ID', 'Restaurant Name', 'Country Code', 'City', 'Address', 'Locality',
         'Locality Verbose', 'Longitude', 'Latitude', 'Cuisines', 'Average Cost for two', 'Currency',
          'Has Table booking', 'Has Online delivery', 'Is delivering now', 'Switch to order menu',
           'Price range','Aggregate rating', 'Rating text', 'Votes']
csv_writer.writerow(header)

for restaurants in file1_data:

    restaurant = restaurants['restaurant']
    restaurantValues = [	restaurant['R']['res_id'] ,
	                        restaurant['name'],
	                        restaurant['location']['country_id'],
	                        restaurant['location']['city'],
	                        restaurant['location']['address'],
	                        restaurant['location']['locality'],
	                        restaurant['location']['locality_verbose'],
	                        restaurant['location']['longitude'],
	                        restaurant['location']['latitude'],
                            restaurant['cuisines'],
                            restaurant['average_cost_for_two'],
                            restaurant['currency'],
                            restaurant['has_table_booking'],
                            restaurant['has_online_delivery'],
                            restaurant['is_delivering_now'],
                            restaurant['switch_to_order_menu'],
                            restaurant['price_range'],
                            restaurant['user_rating']['aggregate_rating'],
                            restaurant['user_rating']['rating_text'],
                            restaurant['user_rating']['votes']
                                                ]
    
    csv_writer.writerow(restaurantValues)
        

zomato_csv.close()

