#imports openAI from many modules available in langchain package
from langchain_openai import OpenAI

#imports load_dotenv function from dotenv package to load environment variables from a .env file (basically for security purposes- the API keys are stored in .env file)
from dotenv import load_dotenv    

load_dotenv()  # Load environment variables from .env file

llm=OpenAI(model="gpt-3.5-turbo")  #creates an instance of OpenAI class with specified model (gpt-3.5-turbo in this case)

result=llm.invoke("What is the capital of India?")  #invokes the model with a prompt to get the capital of India
 
print(result)  #prints the result obtained from the model

