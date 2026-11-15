import os
import numpy
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

def get_embedding(text):
    response = client.embeddings.create(
        model = os.getenv("EMBEDDING_MODEL"),
        input = text
    )
    return response.data[0].embedding

def cosine_similarity(A, B):
   dotproduct =  numpy.dot(A,B),
   lenA = numpy.linalg.norm(A),
   lenB = numpy.linalg.norm(B)
   mulLen = numpy.dot(lenA,lenB)
   similarity =  dotproduct/mulLen
   return similarity

text1 = "Iam Learning AI with codestorywithMIK"
text2 = "Experimenting with embeddings"
text3 = "embeddings capture semantic relationship"

emb1 = get_embedding(text1)
emb2 = get_embedding(text2)
emb3 = get_embedding(text3)
result1 = cosine_similarity(emb1,emb2)
result2 = cosine_similarity(emb2,emb3)
print(f"cosine similar between text1 : {text1} and text2 : {text2} is {result1.item():.2f}")
print(f"cosine similar between text2 : {text2} and text3 : {text3} is {result2.item():.2f}")



    
# cosine similar between Iam Learning AI with codestorywithMIK and Experimenting with embeddings is [0.51509934]
# cosine similar between Experimenting with embeddings and embeddings capture semantic relationship is [0.72807436] ==> close to 1 similar text2 and text3