import os
from types import SimpleNamespace
from openai import OpenAI
from dotenv import load_dotenv
from tools import TOOLS,run_tool

load_dotenv()


calls = {} # dictionru index -> tool call(object) being built
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)
message = [{"role":"user","content":"can you tell me weather in new york city today and seattle and south korea?"}]

stream = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = message,
    tools = TOOLS,
    stream = True
)

full_response = ""
for event in stream:
    if not event.choices: #some server will sendchunks with no choices
        continue
    piece = event.choices[0].delta
    for tool_call in (piece.tool_calls or []):
        obj = calls.setdefault(
            tool_call.index, 
            SimpleNamespace(id = None, function = SimpleNamespace(name = "", arguments=""))
            ) #SimpleNamespace is a built-in utility class in Python’s types module that lets you create lightweight objects to store and access attributes using dot notation
        if tool_call.id:
            obj.id = tool_call.id
        if tool_call.function and tool_call.function.name:
            obj.function.name += tool_call.function.name
        if tool_call.function and tool_call.function.arguments:
            obj.function.arguments += tool_call.function.arguments

print(calls)
call_list = []
for key in sorted(calls):
    call_list.append(calls[key])

for tool_call in call_list:
    result = run_tool(tool_call)
    message.append({"role":"tool","content": result})



stream = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = message,
    stream = True
)

for event in stream:
    if not event.choices:
        continue
    piece = event.choices[0].delta
    if piece.content:
        #print(piece.content, end = "", flush = True)
        full_response += piece.content
print("\n\nFull response: " + full_response)

# [ChoiceDeltaToolCall(index=0, id='call_v3tph87x', function=ChoiceDeltaToolCallFunction(arguments='{"city":"New York City"}', name='get_weather'), type='function')]
# [ChoiceDeltaToolCall(index=1, id='call_cgi6qjg9', function=ChoiceDeltaToolCallFunction(arguments='{"city":"Seattle"}', name='get_weather'), type='function')]
# [ChoiceDeltaToolCall(index=2, id='call_vnjifed0', function=ChoiceDeltaToolCallFunction(arguments='{"city":"south korea"}', name='get_weather'), type='function')]
# not necessarily it will come at once whole tool response as chunks, it can come in multiple chunks, so we need to handle that in the code. The above print statement will print the tool calls as they come in the stream.