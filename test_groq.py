import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

print("Initializing Groq LLM...")
try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )
    print("LLM Initialized:", llm)
    print("Sending test invoke...")
    res = llm.invoke("Say hello in one word")
    print("Success! Response is:", res)
except Exception as e:
    import traceback
    print("An error occurred:")
    traceback.print_exc()
