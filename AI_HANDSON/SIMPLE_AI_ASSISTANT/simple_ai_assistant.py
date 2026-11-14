#standard library imports (first)
import os
from types import SimpleNamespace  #builtin module of python to access environment variables

#third party imports (second)
from openai import OpenAI # from package of openai we are importing OpenAI class
from dotenv import load_dotenv

#Local module imports (last)
from utility.utility import log #importing the log method from utility.py file 
from tools import TOOLS, run_tool #importing the tools from tools.py file
MAX_TOOL_CALLS = 3


load_dotenv() #loading the environment variables from .env file

# #method get the tools response
# def get_tool_response(msg):
#     for tool_call in msg.tool_calls:
#         result = run_tool(tool_call)
#         log(f" --> 🛠️  Tool response: {result}")
#         messages.append({
#             "role":"tool",
#             "tool_call_id":tool_call.id,
#             "content":str(result)
#         })

messages = []
full_response = ""
# messages.append({"role":"system","content":"Act as a techinal assistant respond with  10 words"})
calls = {} # dictionary index -> tool call(object) being built
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
        stream = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages = messages,
                tools = TOOLS,
                stream = True,
            )
        for event in stream:
            if not event.choices:
                continue
            chunk = event.choices[0].delta
            for tool_call in (chunk.tool_calls or []):
                obj = calls.setdefault(
                    tool_call.index,
                    SimpleNamespace(id=None, function = SimpleNamespace(name="", arguments=""))
                )
                if tool_call.id:
                    obj.id = tool_call.id
                if tool_call.function and tool_call.function.name:
                    obj.function.name += tool_call.function.name
                if tool_call.function and tool_call.function.arguments:
                    obj.function.arguments += tool_call.function.arguments
            # print(calls)
        call_list = []
        for key in sorted(calls):
            call_list.append(calls[key])
        for tool_call in call_list:
            result = run_tool(tool_call)
            messages.append({"role":"tool","content": result})
        stream = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = messages,
            stream = True
            )


        for event in stream:
            if not event.choices:
                continue
            piece = event.choices[0].delta
            if piece.content:
                print(piece.content, end = "", flush = True)
                full_response += piece.content
        # print("\n\nFull response: " + full_response)
        
        # #print("\nLLM 1st response with tools of weather"+response)
        # msg = response.choices[0].message
        # if not msg.tool_calls:
        #         break;
        # log(f" step {i+1} LLM response with tool calls: {len(msg.tool_calls)}")
        # messages.append(msg)# we are appending the tool call message to messages list so that we can send it to LLM in next call
        # get_tool_response(msg)
    else:
        log(f"Max tool calls reached ({MAX_TOOL_CALLS}). Stopping further tool calls.")
        fallback = "Sorry, I have reached the maximum number of tool calls. Please try again with a different query."
        print("\n 🤖Assistant: " + fallback)

    messages.append({"role":"Assistant","content":full_response})
    print("\n 🤖Assistant:" + full_response or "")
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