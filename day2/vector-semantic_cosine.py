from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Load environment variables
load_dotenv()
client = OpenAI()

# Step 2: Function to get embeddings (updated for v1.0+)
def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return np.array(response.data[0].embedding)

# some example in text
# Step 3: Example texts
text1 = "I love programming in Python."
text2 = "Python coding is my passion."
text3 = "I enjoy playing football."

# getting the embedding of texts
emb1 = get_embedding(text1)
emb2 = get_embedding(text2)
emb3 = get_embedding(text3)

# calling similarity 
similarity1 = cosine_similarity([emb1], [emb2])
similarity2 = cosine_similarity([emb1], [emb3])
similarity3 = cosine_similarity([emb2], [emb3])

# printing similarity
print(f"Similarity between '{text1}' and '{text2}': {similarity1[0][0]}")
print(f"Similarity between '{text1}' and '{text3}': {similarity2[0][0]}")
print(f"Similarity between '{text2}' and '{text3}': {similarity3[0][0]}")
