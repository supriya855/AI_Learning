import os  #builtin module of python to access environment variables
from dotenv import load_dotenv #from package of dotenv we are importing load_dotenv function
load_dotenv() #loading the environment variables from .env file
from openai import OpenAI # from package of openai we are importing OpenAI class
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

messages = []
messages.append({"role":"system","content":"Act as a techinal assistant respond with 10 words"})
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
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages = messages
    )
    print("LLM Response:")
    print("Assistant :"+ response.choices[0].message.content)
    print(response.choices[0].message.role)
    messages.append({"role":"assistant","content":response.choices[0].message.content})