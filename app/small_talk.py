from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

groq_Client = Groq()

small_talk_sys_prompt = """
    You are a helpful and friendly chatbot designed for small talk. You can answer questions about the weather, your name, your purpose, and more
"""

def small_talks_query(query):

    chat_completion = groq_Client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content": small_talk_sys_prompt
            },
            {
                "role":"user",
                "content": query
            }
        ],
        model=os.environ['GROQ_MODEL'],
        temperature=0.2,
        max_tokens=1024
    )

    return chat_completion.choices[0].message.content

if __name__=="__main__":
    print(small_talks_query("Hello how are you ?"))