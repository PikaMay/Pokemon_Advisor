from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

data_path = './pokemon_data/gen01.csv'
df_csv = pd.read_csv(data_path)

# Embed the CSV data file 
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Create the vector database location 
embeddings_db = "./db/vector_pokemon_db"
save_documents = not os.path.exists(embeddings_db)

# Preparing the documents to be converted
if save_documents:
    documents = []
    ids = []

    for i, row in df_csv.iterrows():
        doc_text = f"""
{row['Name']} is a Generation {row['Generation']} Pokémon.
It is a {row['Type1']} with the following stats:
HP: {row['HP']}, Attack: {row['Attack']}, Defense: {row['Defense']},
Special Attack: {row['Sp. Atk']}, Special Defense: {row['Sp. Def']}, Speed: {row['Speed']}.
Its totale base stats add up to {row['Total']}

"""
        document = Document(
            page_content=doc_text,
            metadata={
                "Name": row["Name"], 
                "Type1": row["Type1"],
                "Type2": row["Type2"],
                "Generation": row["Generation"]
            },
            id=str(i)
        )

        ids.append(str(i))
        documents.append(document)

# Creating the vector store
vector_store = Chroma(
    collection_name="pokemon_data",
    persist_directory=embeddings_db,
    embedding_function=embeddings
)

if save_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Make the vector store accessible by the LLM
# Retirever helps into looking up for documents
retriever = vector_store.as_retriever(
    search_kwargs={"k": 15} # nbre of documents to look for = 5, 5 reviews 
)