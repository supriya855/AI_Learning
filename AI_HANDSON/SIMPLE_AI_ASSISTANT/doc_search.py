import os
import numpy
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)

EMBED_MODEL = os.getenv("EMBEDDING_MODEL")
KB_FOLDER = os.getenv("KB_FOLDER")

#step - 1 Load the documents

def load_documents(folder = KB_FOLDER):
    documents = []
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder,filename)
        #with is used to  help to close the file automatically once read operation is done
        with open(path,"r",encoding="utf-8") as f:
            documents.append({
                "source":filename,
                "text":f.read()
            })
    # print(documents)
    return documents

def get_embedding(text):
    response = client.embeddings.create(
        model = EMBED_MODEL,
        input = text
    )
    return response.data[0].embedding

def cosine_similary(A, B):
    dot_prod =numpy.dot(A,B)
    norm_a = numpy.linalg.norm(A)
    norm_b = numpy.linalg.norm(B)
    return dot_prod/ (norm_a * norm_b)

# step -2 Add the embedding in the documents

def add_embedding(documents):
    for doc in documents:
        vector = get_embedding(doc["text"])
        doc["vector"] = vector
    return documents

def search(query, documents,top_k =3):
    query_vector = get_embedding(query)
    results = []
    for doc in documents:
        score = cosine_similary(query_vector,doc["vector"])
        results.append({
            "score":float(score),
            "source":doc["source"],
            "text":doc["text"],
            "size":len(doc["text"])

        })
    #lambda is anonymous function you can define without explicitly giving its function name
    results.sort(key = lambda rec : rec["score"], reverse=True) #basically it sorts in ascending order with reverse True will get Desc order top3 scores we can pick easily
    return results[:top_k]

def test(user_query, documents, top_k=3):
    print(f"User Query : {user_query}")
    results = search(user_query, documents, top_k=3)
    for r in results:
        print(f"Score : {r['score']:.2f} - Source : {r['source']} - Size : {r['size']}")

documents = load_documents()
print(documents[0])
documents = add_embedding(documents)

print(f"We have embedded {len(documents)} documents")

user_query = "How many sick leaves are present in total?"

test(user_query,documents,3)

