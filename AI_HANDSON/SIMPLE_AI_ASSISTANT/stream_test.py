import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

stream = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = [
        {
            "role": "user",
            "content": "can you explain me python in 50 words!"
        }
    ],
    stream = True
)
full_response = ""
for event in stream:
    # print(event)
    # print("\n\n----------------------------\n\n")
    chunk = event.choices[0].delta.content
    if(chunk):
        print(chunk, end = "", flush = True)
        full_response +=chunk
        #python print function is used to print the content of the event in the console. The end = "" argument is used to avoid adding a new line after each print statement. The flush = True argument is used to force the output to be printed immediately, rather than being buffered. This is useful when streaming data, as it allows the user to see the output in real-time.

print("\n\nFull response: " + full_response)

