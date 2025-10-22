from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

llm = HuggingFaceEndpoint(
  repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",
)

mode = ChatHuggingFace(llm=llm)
result = mode.invoke("what is the capital of France?")
print(result)