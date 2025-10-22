from langchain_google_geneai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

model=ChatGoogleGenerativeAI(model_name="gemini-2.5-flash", temperature=0, max_completions_tokens=10)

result = model.invoke("what is the capital of France?")
print(result)