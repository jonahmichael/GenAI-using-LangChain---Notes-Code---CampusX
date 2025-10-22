# claude is also paid
# so we will write code but we won't run it here

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

model=ChatAnthropic(model_name="claude-2", temperature=0, max_completions_tokens=10)
result = model.invoke("what is the capital of France?")
print(result)