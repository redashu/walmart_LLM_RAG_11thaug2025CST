# importing required modules 
import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

import os
from dotenv import load_dotenv
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
# testing api KEy 
client = OpenAI()


# loading csv file 
df=pd.read_csv('user.csv')
df.info()
df.head(3)

# converting dataframe to Langchain document 
loader = DataFrameLoader(df, page_content_column="name")
data = loader.load()

# before embedding we need to tokenization 
# Step 3: Split into chunks (though small, we'll treat each row as a chunk)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)
chunks = text_splitter.split_documents(data)


# now calling openai Text embedding model to convert token into vector
# Step 5: Create embeddings with explicit API key
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")  # or use the direct variable
)

