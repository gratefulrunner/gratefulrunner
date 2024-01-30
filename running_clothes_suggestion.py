from pip._vendor import requests
import json

api_key = 'xyz'
base_url = 'http://api.openweathermap.org/data/2.5/weather?zip='

#program inputs

location = input ("Hey Sam. Time to run! Are you at home today? ")
if location == 'y' or location == 'yes' or location == 'Y' or location == 'Yes' or location == 'Yes!' or location == 'YEs':
    home_location = input("LI or NYC? ") 
    if home_location == 'li' or home_location =='LI' or home_location == 'Long Island':
        zip_code = xyz #Long Island Zip Code that I run at frequently
    elif home_location != 'li' or home_location != 'LI' or home_location != 'Long Island':
        zip_code = xyz #NYC Zip Code that I run at Frequently
    print ('\n'+ "Welcome home Sam! Great day to be in the "+ str(zip_code)+'\n')
elif location != 'y' or location !='yes' or location !='Yes':
    zip_code = input ("Fun! A new place to run. What zip are you in today? "+ '\n')
try:
    int(zip_code)
except:
    print ('Your input is invalid. Please try again.')

#api connection
final_url = base_url + str(zip_code) +"&appid=" + api_key + "&units=imperial"
get_data = requests.get(final_url).json()


#json transformation
dict_json = json.dumps(get_data)
read_json = json.loads(dict_json)
city_name = (read_json["name"])


#temperature data like humidity, feels like, etc.
temp_layer =  (read_json["main"])
dict_temp_layer = json.dumps(temp_layer)
read_temp_layer = json.loads(dict_temp_layer)
current_temp= (read_temp_layer["temp"])
current_feels= (read_temp_layer["feels_like"])
current_hum= (read_temp_layer["humidity"])
temp_var = (current_temp- current_feels)
wind_layer = (read_json["wind"])
wind_speed = (wind_layer["speed"])


#weather description data
description_layer = (read_json["weather"])
weather_description = (description_layer[0]["description"])


#second API call parameters and addresses
base_uv_url = 'https://api.openweathermap.org/data/2.5/onecall?lat='
lat_long_data = (read_json["coord"])
lat = (lat_long_data["lat"])
lon = (lat_long_data["lon"])
exclusions = 'minutely,hourly,daily'
second_api_url = base_uv_url + str(lat)+ '&lon=' + str(lon)  +'&exclude=' + exclusions  + '&appid=' + api_key
get_uvi = requests.get(second_api_url).json()
current = (get_uvi["current"])
uvi = (current["uvi"])


#accessory logic
if uvi >=6 :
    sunscreen = 'Today, Sunscreen or a hat with a brim will come in handy. ' 
elif uvi <6:    
    sunscreen = ""
if current_temp > 45 and current_temp <=50 and current_hum <80 or current_temp <=45 and current_feels <=45 or current_temp <=50 and current_hum <80 and wind_speed >=10:
    gloves = 'You should Wear Gloves out there- its pretty chilly or windy. '
else:
    gloves = ""
if weather_description == 'broken clouds' or weather_description == 'clear sky':
    sunglasses = 'You may want to wear sunglasses today'
else:
    sunglasses = ''


#shirt logic
if current_feels >=70 and current_feels <80 and humidity >=70:
    shirt = "The running sage bot recommends that you wear either a t-shirt or a tank top. It's a humid one, so maybe go with the tank. "
if current_feels >= 80 or current_feels >=80 and humidity >=0:
    shirt = "It's a really hot day today. Wear a tank "
if current_feels < 70 and current_feels >=60 and humidity <80:
    shirt = 'A t-shirt should be fine for today! '
elif current_feels < 70 and current_feels >= 60 and humidity >=80:
    shirt = "It's cool enough to wear a t-shirt, but it is very humid. Maybe go with a tank. "
if current_feels <60 and current_feels >= 50 and humidity >=80 and wind_speed <10:
    shirt = "It's cool out but humidity is high. Go with a T-shirt. "
elif current_feels <60 and current_feels >= 50 and humidity <80:
    shirt = "Wear a Long sleeve shirt."
if current_feels <50 and current_feels >=45 and wind_speed >=5 and humidity >=75:
    shirt = "It's cold out but incredibly humid. Consider a T shirt or just a long sleeve."
if current_feels <50 and current_feels >=45 and wind_speed >=5 and humidity <75:
    shirt = "You may want to wear two layers today. A Tech tee and cotton Long sleeve would be good."
elif current_feels <50 and current_feels >=45 and wind_speed <5:
    shirt = "It's Cold but not very windy. A single layer long sleeve should do the trick!"
if current_feels >=40 and current_feels <45 and wind_speed <5:
    shirt = "It's Cold out, but not very windy. A Tech tee and cotton long sleeve is good for today."
elif current_feels >=40 and current_feels <45 and wind_speed >=5:
    shirt = "It's cold out with some wind. Today, A long sleeve tech with long sleeve cotton is advisable."
if current_feels >=35 and current_feels <40 and wind_speed <5:
    shirt = "It's nearly freezing today, but not very windy. Long sleeve tech and a warm long sleeve cotton is advisable."
elif current_feels >=35 and current_feels <40 and wind_speed >=5:
    shirt = "It's cold out today, and there is some wind. ShirtBot would go with a short sleeve tech and a sweatshirt."
if current_feels <35 and current_feels >=30 and wind_speed <5:
    shirt = "It's very cold out today, but not much wind. ShirtBot would recommend a short sleeve tech and a sweatshirt"
elif current_feels >=30 and current_feels <35 and wind_speed >= 5:
    shirt = "It's very cold, with considerable wind. Long sleeve tech and sweathsirt is the move."
if current_feels < 30 and current_feels >= 25 and wind_speed <5:
    shirt = "It's freezing today. ShirtBot recommends a long sleeve tech and a sweatshirt"
elif current_feels < 30 and current_feels >= 25 and wind_speed >=5:
    shirt = "It's freezing today, with wind. ShirtBot recommends considering three layers- possibly two shirts and either a jacket or sweatshirt."
if current_feels <25:
    shirt = "It's very cold today. Wear two warm base layers and either a sweatshirt or jacket."
    

#pants logic
if current_feels >=30 and wind_speed <=10:
    pants = 'You should be good with Shorts. Almost Always!'
elif current_feels >=30 and current_feels <35 and wind_speed >10:
    pants = 'Temps could be good for shorts. But it is super windy. Consider sweats or tights.'
if current_feels < 30:
    pants = "It's super cold out. Consider sweats or tights for your run today."
        


#weather report string
weather_report_output = "Weather conditions in "+str(city_name)+ " is " + weather_description + " right now. The temperature is "+ str(current_temp) + " degrees farenheit. "+"The Feels Like Temperature is "+str(current_feels)+ " Degrees Farenheit. Humidity is "+str(current_hum) +"%." +" Wind is speed is " + str(wind_speed) + " miles per hour."
        

print ('\n' +'\n' + "It's always a Great day for a run! " )


#weather report logic
weather_report_selection = input("Woud you like to see a full weather report? ")
if weather_report_selection == 'y' or weather_report_selection == 'Y' or weather_report_selection == 'yes' or weather_report_selection == 'Yes' or weather_report_selection == 'YES':
    print ('\n'+ weather_report_output + '\n' +'\n' + 'Loading clothing suggestions now... '+ '\n'+ '\n')
else:
    print('\n'+ 'Got it! Loading clothing suggestions now... '+ '\n'+ '\n')


#suggestion output
print (sunscreen + gloves + sunglasses + '\n' + '\n')
print (shirt+ '\n'+ '\n'+ pants)
