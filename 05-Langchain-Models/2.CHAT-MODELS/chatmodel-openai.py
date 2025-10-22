from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

model=ChatOpenAI(model_name="gpt-4")
result = model.invoke("what is the capital of France?")
print(result)

# Expected output: "The capital of France is Paris."