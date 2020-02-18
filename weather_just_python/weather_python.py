import requests, json
from requests import *

api_key = "b035d121ff439c272df931cfce3dbeec"
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
##########################____ START PROGRAM ____##########################
cont  = True
while(cont):
    city_name = input("Enter city name: ")
    complete_url = base_url+"q="+city_name+"&appid="+api_key
    response = requests.get(complete_url)
    # response = requests.get('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
    x = response.json()
    if x['cod'] != "404":
        y = x['main']
        cur_temp = round((y["temp"] - 273.15),1)   # Cencius
        cur_press = y['pressure']
        cur_humid = y['humidity']
        z = x['weather']
        weather_des = z[0]['description']
        print('\n',"*"*50,city_name ,"*"*50,'\n')
        print('\t'+"temperature : "+str(cur_temp) +'_C'+ '\n'+
                '\t'+"pressure : " +str(cur_press)+'_hPa'+'\n'+
                '\t'+"humidity : " +str(cur_humid)+'_%'+'\n'+
                '\t'+"description : " +str(weather_des)+'\n'
            )
        print('\n',"*"*50,"  ____  " ,"*"*50,'\n')
    else:
        print('city not found! ')
    continue_pr = input('continue with "y" ? ')
    if continue_pr != 'y':
        cont = False

print('\n',"*"*50,"___ exit the programe ___" ,"*"*50,'\n')
