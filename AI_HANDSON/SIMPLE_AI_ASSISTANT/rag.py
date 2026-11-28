import os
import numpy
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)
EMBED_MODEL = os.getenv("EMBEDDING_MODEL")
KB_FOLDER = os.getenv("KB_FOLDER")

#get the embeddings
def get_embeddings(text):
    response = client.embeddings.create(
        model = EMBED_MODEL,
        input = text
    )
    return response.data[0].embedding

#add embeddings
def add_embeddings(chunks):
    for chunk in chunks:
        vector = get_embeddings(chunk['text'])
        chunk['vector'] = vector
    return chunks



#cosine similarity
def cosine_similarity(A,B):
    dot_prod = numpy.dot(A,B)
    norm_a = numpy.linalg.norm(A)
    norm_b = numpy.linalg.norm(B)
    return dot_prod / (norm_a*norm_b)

#load_documents which are present in knowledge base
def load_documents(folder = KB_FOLDER):
    documents = []
    for file_name in sorted(os.listdir(folder)):
        print(file_name)
        path = os.path.join(folder,file_name)
        with open(path,"r",encoding="utf-8") as f:
            documents.append(
                {
                "source": file_name,
                "text": f.read()
                }

            )
    return documents

# create the chunks
def create_chunks(documents):
    chunks = []
    chunk_id =0
    for text in documents['text'].split("\n"): 
        text = text.strip() # it removes the unnecessary spaces
        chunks.append(
            {
                "source": documents["source"],
                "text" : text,
                "chunk_id":chunk_id
            }
        )
        chunk_id+=1
    return chunks


# we are getting the score the cosine similarity from user_query and with existing chunks
# and getting the top-k results
def search(user_query,chunks,top_k =3):
    user_query_embed = get_embeddings(user_query)
    results = []
    for chunk in chunks:
        score = cosine_similarity(user_query_embed,chunk['vector'])
        results.append(
            {
                "score":float(score),
                "source":chunk['source'],
                "chunk_id":chunk['chunk_id'],
                "text":chunk['text'],
                "size":len(chunk['text'])
            
            }
        )
    print("entered search and trying resu")
    # print("results", results)
    results.sort(key = lambda res: res["score"] , reverse=True)
    return results[:top_k]

def test(user_query,folder):
    chunks = []
    loaded_doc = load_documents(folder)
    for doc in loaded_doc:
        chunks.extend(create_chunks(doc))
    # print(chunks)

    results = search(user_query, chunks, 3)
    # print(results)
    for r in results:
        print(f"Chunked id :  {r['chunk_id']} text : {r['text']}  size : {r['size']}")


# top3 chunks which matches the user query
user_query = "How many days of sick leave"
test(user_query,folder=KB_FOLDER)



