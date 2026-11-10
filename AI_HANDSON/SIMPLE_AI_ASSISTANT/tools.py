from datetime import datetime
import json
import requests
from utility.utility import log
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url,timeout =10)
    response.raise_for_status()  # Raise an exception for HTTP errors (like if network is down or city not found)
    print(response)
    return response.text
def get_city_user():
    return "HYDERABAD"

def run_tool(tool_call):
    fun_name = tool_call.function.name
    tool_args = tool_call.function.arguments
    try:
        fn_args = json.loads(tool_args or "{}") # its in string of json ex: '{}' converting to dictionary 
        fn = FUNCTION_NAME_FUNCTION_METHOD[fun_name]
        log(f" -> 🛠️ Tool call: {fun_name} with arguments: {tool_args}")
        result = fn(**fn_args)#convert key value separately
    except Exception as e:
        result =f"Error occurred while calling function {fun_name}: {e}"
        exit(1)
    return str(result)    
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
                },
                "required":["city"]
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