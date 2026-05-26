import os
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

print("Initializing ChatMistralAI with Sarvam endpoint...")
try:
    llm = ChatMistralAI(
        model="sarvam-2b-v0.5",
        endpoint="https://api.sarvam.ai/v1",
        mistral_api_key=os.getenv("SARVAM_API_KEY"),
        temperature=0.3
    )
    print("LLM Initialized:", llm)
    print("Sending test invoke to Sarvam...")
    res = llm.invoke("Say hello in one word")
    print("Success! Response is:", res)
except Exception as e:
    import traceback
    print("An error occurred:")
    traceback.print_exc()
