import os
import numpy
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

EMBED_MODEL = os.getenv("EMBEDDING_MODEL")
KB_FOLDER = os.getenv("KB_FOLDER")
VECTOR_STORE_DB = os.getenv("VECTOR_STORE_DB")

def get_embeddings(text):
    response = client.embeddings.create(
        model = EMBED_MODEL,
        input = text
    )
    return response.data[0].embedding
    

def cosine_similarity(A, B):
    dot_prod = numpy.dot(A,B)
    mod_A = numpy.linalg.norm(A)
    mod_B = numpy.linalg.norm(B)
    return dot_prod / (mod_A * mod_B)



def load_document(folder=KB_FOLDER):
    documents = []
    for filename in sorted(os.listdir(folder)):
        path = os.path.join(folder,filename)
        with open(path,"r",encoding="utf-8") as f:
            documents.append(
                {
                    "source":filename,
                    "text":f.read()
                }
            )
    return documents

def add_embedding(chunks):
    for chunk in chunks:
        vector = get_embeddings(chunk["text"])
        chunk["vector"] = vector
    return chunks

def search(query,chunks, top_k = 3):
    query_vector = get_embeddings(query)
    results = []
    for chunk in chunks:
        score = cosine_similarity(query_vector,chunk["vector"])
        results.append(
            {
                "score":float(score),
                "source":chunk["source"],
                "chunk_id":chunk["chunk_id"],
                "text":chunk["text"],
                "size":len(chunk["text"])

            }
        )
    results.sort(key = lambda rec : rec["score"], reverse=True) #basically it sorts in ascending order with reverse True will get Desc order top3 scores we can pick easily
    return results[:top_k]

def test(user_query,chunks,top_k=3):
    print(f"User Query : {user_query}\n")
    results = search(user_query,chunks,top_k)
    for r in results:
        print(f"Score : {r['score']:.2f} - Source : {r['source']} - Size : {r['size']}")
        print(f" {r['text']}")


def chunk_document(document):
    chunks=[]
    chunk_id = 0
    for text in document["text"].split("\n"):
        text = text.strip()
        if text:
            chunks.append({
                "source":document["source"],
                "chunk_id":chunk_id,
                "text":text
            })
            chunk_id +=1
    return chunks
            

    


def create_chunk():
        documents = load_document()
        chunks= []
        for doc in documents:
            chunks.extend(chunk_document(doc))
        return chunks

def save_to_vector_store(chunks):
    with open(VECTOR_STORE_DB,"w",encoding="utf-8") as f:
        json.dump(chunks,f,indent = 4)
    
def load_vector_store():
    with open(VECTOR_STORE_DB,"r",encoding="utf-8") as f:
       return json.load(f) 

chunks = []

if os.path.exists(VECTOR_STORE_DB):
    chunks = load_vector_store()
    print(f"Loaded {len(chunks)} chunks from the vecore store files in DB {VECTOR_STORE_DB}")
else:
    chunks = create_chunk()
    chunks = add_embedding(chunks)
    save_to_vector_store(chunks)
    print(f"Created and embedded {len(chunks)} chunks and saved to the vector store file {VECTOR_STORE_DB}")

print(f"we have embdedd {len(chunks)} chunks from our knowledge base")

user_query = "How many sick leaves are present in total"
test(user_query,chunks,3)


# 1st time hit (it created the vector_store.json and write the chunks to it) python .\chunk_search.py
# Created and embedded 38 chunks and saved to the vector store file knowledge_base\vector_store.json
# we have embdedd 38 chunks from our knowledge base
# User Query : How many sick leaves are present in total

# Score : 0.69 - Source : leave_policy.txt - Size : 200
#  Every full-time employee is entitled to 18 earned leaves, 12 sick leaves, and 6 casual leaves per calendar year. Employees can carry forward a maximum of 10 unused earned leaves to the following year.
# Score : 0.65 - Source : leave_policy.txt - Size : 92
#  Employees taking more than three consecutive sick leaves must provide a medical certificate.
# Score : 0.62 - Source : leave_policy.txt - Size : 76
#  Unused sick leaves and casual leaves expire at the end of the calendar year.



# (2nd time it loaded the chunks from the file it stored) python .\chunk_search.py
# Loaded 38 chunks from the vecore store files in DB knowledge_base\vector_store.json
# we have embdedd 38 chunks from our knowledge base
# User Query : How many sick leaves are present in total

# Score : 0.69 - Source : leave_policy.txt - Size : 200
#  Every full-time employee is entitled to 18 earned leaves, 12 sick leaves, and 6 casual leaves per calendar year. Employees can carry forward a maximum of 10 unused earned leaves to the following year.
# Score : 0.65 - Source : leave_policy.txt - Size : 92
#  Employees taking more than three consecutive sick leaves must provide a medical certificate.
# Score : 0.62 - Source : leave_policy.txt - Size : 76
#  Unused sick leaves and casual leaves expire at the end of the calendar year.

