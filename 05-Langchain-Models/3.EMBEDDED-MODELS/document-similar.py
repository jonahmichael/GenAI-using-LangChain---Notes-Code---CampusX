from langchain-openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity # to compute cosine similarity
import numpy as np 

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents=["Delhi is the capital of India", "Paris is the capital of France", "Tokyo is the capital of Japan", "Canberra is the capital of Australia", "Ottawa is the capital of Canada", "Berlin is the capital of Germany"]

# Embed the documents
doc_embeddings=embedding.embed_documents(documents)
# Embed a query
query_embedding=embedding.embed_query("Paris is the capital of France")
# Compute cosine similarities between the query and document embeddings
similarities = cosine_similarity([query_embedding], doc_embeddings)
print(similarities)

# Sort the documents based on similarity scores
print(sort(list(enumerate(cosine_similarity([query_embedding], doc_embeddings)[0])),key=lambda x:x[1],reverse=True))

