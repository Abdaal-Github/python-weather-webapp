from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Istanbul"):
    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("api_key")}&q={city}&units=imperial'
    
    weather_data=requests.get(request_url).json()
    
    return weather_data

if __name__=="__main__":
    
    print("\n***** Get Current Weather*****\n")
    city=input("\nEnter the name of the city: ")
    
    #check for empty 
    if not bool(city.strip()):
        city="Peshawar"
    
    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)
    