import json
import os  #builtin module of python to access environment variables
from dotenv import load_dotenv #from package of dotenv we are importing load_dotenv function
load_dotenv() #loading the environment variables from .env file
from openai import OpenAI # from package of openai we are importing OpenAI class
from tools import TOOLS,FUNCTION_NAME_FUNCTION_METHOD #importing the tools from tools.py file


messages = []
messages.append({"role":"system","content":"Act as a techinal assistant respond with  10 words"})
while True:
    user_input = input("\nME:")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat...")
        break
    messages.append({"role":"user","content":user_input})
    client = OpenAI(
        base_url=os.getenv("BASE_URL"),
        api_key=os.getenv("API_KEY")
    )
    #1st call to LLM with tools
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages = messages,
        tools = TOOLS
    )
    print("\nLLM 1st response with tools of weather"+ (str)(response))
    msg = response.choices[0].message
    if msg.tool_calls:
        messages.append(msg)# we are appending the tool call message to messages list so that we can send it to LLM in next call
        for tool_call in msg.tool_calls:
            fun_name = tool_call.function.name
            tool_args = tool_call.function.arguments
            fn_args = json.loads(tool_args or "{}") # its in string of json ex: '{}' converting to dictionary 
            fn = FUNCTION_NAME_FUNCTION_METHOD[fun_name]
            result = fn(**fn_args)#convert key value separately
            messages.append({
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content":str(result)
            })
        #2nd call to LLM with tool results    
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )
        msg = response.choices[0].message
    messages.append({"role":msg.role,"content":msg.content})
    print("\nAssistant:" + msg.content)
    # print("\n\n----------------------------\n\n")
    # print("Messages so far:")
    # print(response)
        




# client = OpenAI(
#     base_url="http://127.0.0.1:11434/v1",#ollama serve
#     api_key ="dummy_api_key"
# )
# response = client.chat.completions.create(
#     model ="qwen3:4b",
#     messages = [
#         {
#             "role": "user",
#             "content": "Hello LLM!!"
#         }
#     ]
# )
# client = OpenAI(
#     base_url=os.getenv("BASE_URL"),
#     api_key=os.getenv("API_KEY")
# )
# response = client.chat.completions.create(
#     model=os.getenv("MODEL"),
#     messages = [
#         {
#             "role": "user",
#             "content": "Hello LLM!!"
#         }
#     ]
# )
# print("LLM Response:")
# print(response.choices[0].message.content)