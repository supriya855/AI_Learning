#standard library imports (first)
import os  #builtin module of python to access environment variables

#third party imports (second)
from openai import OpenAI # from package of openai we are importing OpenAI class
from dotenv import load_dotenv
from types import SimpleNamespace

#Local module imports (last)
from utility.utility import log #importing the log method from utility.py file 
from tools import TOOLS, run_tool #importing the tools from tools.py file
MAX_TOOL_CALLS = 3


load_dotenv() #loading the environment variables from .env file

def stream_chat(messages):
    """
    Stream_chat for steaming the messages one by one content and tools
    """
    try:
        calls_list = []
        calls ={}
        full_response = ""
        stream = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = messages,
            tools = TOOLS,
            stream = True
        )
        label_print = False
        for chunk in stream:
            if not chunk.choices:
                continue
            #1 for content
            piece = chunk.choices[0].delta
            if piece.content:
                if not label_print:
                    print("Assistant : " ,end ="", flush = True)
                    label_print = True
                print(piece.content,end ="",flush = True)
                full_response += piece.content
            #2 for tools (group every tool call responses streams)
            for tool_call in (piece.tool_calls or []):
                obj = calls.setdefault(
                        tool_call.index,
                        SimpleNamespace(id = None, function = SimpleNamespace(name = "",arguments = ""))
                )
                if tool_call.id:
                    obj.id = tool_call.id
                if tool_call.name:
                    obj.name += tool_call.name
                if tool_call.arguments:
                    obj.arguments += tool_call.arguments
    except KeyboardInterrupt:
        print("\n Stopped by User")
        calls = {}
    for key in sorted(calls):
        calls_list.append(calls[key])
    return  full_response, calls_list 


def payload_tool_calls(tool_calls):
    """
    Converts a list of tool call objects into a payload format suitable for sending to the LLM.
    Each tool call object is expected to have an 'id', 'function.name', and 'function.arguments'.
    The function returns a list of dictionaries, each representing a tool call in the required format.
    """
    payload = []
    for tool_call in tool_calls:
         payload.append({
               "id":tool_call.id,
              "type":"function",
              "function":{
                  "name":tool_call.function.name,
                  "arguments":tool_call.function.arguments
              }
         })
    return payload

messages = []
messages.append({"role":"system","content":"Act as a techinal assistant respond with 100 words"})
while True:
    user_input = input("\n🐥 ME:")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat...")
        break
    messages.append({"role":"user","content":user_input})
    client = OpenAI(
        base_url=os.getenv("BASE_URL"),
        api_key=os.getenv("API_KEY")
    )

    #chained tool call or agent loop, we are calling the LLM multiple times until it stops calling the tools or reaches the max tool calls limit
    for i in range(MAX_TOOL_CALLS):
        full_response, tool_calls = stream_chat(messages)
        
        if not tool_calls:
                break
        log(f" step {i+1} LLM response with tool calls: {len(tool_calls)}")
        
        messages.append({
             "role":"Assistant",
             "content":full_response,
             "tool_calls":payload_tool_calls(tool_calls)})
        
        for tool_call in tool_calls:
            result = run_tool(tool_call)
            messages.append(
                {
                    "role":"tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                    }
                )
    else:
        log(f"Max tool calls reached ({MAX_TOOL_CALLS}). Stopping further tool calls.")
        fallback = "Sorry, I have reached the maximum number of tool calls. Please try again with a different query."
        print("\n 🤖Assistant: " + fallback)

    # messages.append({"role":"Assistant","content":full_response})
    # print("\n 🤖Assistant:" + str(full_response) or "")
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