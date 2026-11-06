from datetime import datetime
import requests
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url,timeout =10)
    print(response)
    return response.text
def get_city_user():
    return "HYDERABAD"
#TOOLS we need to add

TOOLS = [
    {
        "type": "function",
        "function" : {
            "name":"get_current_time",
            "description":"Get the current date and time in the format YYYY-MM-DD HH:MM:SS",
            "parameters":{
                "type" : "object",
                "properties" : {},
            }

        }
    },
    {
        "type":"function",
        "function" : {
            "name":"get_weather",
            "description":"Gets the current weather for a given city",
            "parameters" : {
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"The name of the city to get the weather for"
                    }
                }
            }
        }
    },
    {
        "type":"function",
        "function" : {
            "name":"get_city_user",
            "description":"Gets the city of the user when asked for city i live in or my city or where i live or my location or my home",
            "parameters":{
                "type":"object","properties":{}
            }
        }
    }
]
FUNCTION_NAME_FUNCTION_METHOD ={
    "get_current_time": get_current_time,
    "get_weather":get_weather,
    "get_city_user":get_city_user
}