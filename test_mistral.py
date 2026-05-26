import os
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

print("Initializing LLM...")
try:
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0.3
    )
    print("LLM Initialized:", llm)
    print("Sending test invoke...")
    res = llm.invoke("Say hello")
    print("Success! Response is:", res)
except Exception as e:
    import traceback
    print("An error occurred:")
    traceback.print_exc()
