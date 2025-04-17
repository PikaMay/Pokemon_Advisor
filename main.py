from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_search import retriever

# Initialize the model
model = OllamaLLM(model="llama3.2")

template = """
You are a knowledgeable Pokémon trainer.
Here are some Pokémon data entries to consider: {pokemon_entries}

Now, answer the user's question: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("--------------- \n")
    question = input("⚡ Ask your Pokémon question (or q to quit) ⚡:")
    print("\n\n")
    if question.lower == "q":
        break
    
    # Vector search for relevant Pokémon
    docs = retriever.invoke(question)
    
    # Join page_content of each document into a single string
    entries = "\n---\n".join(doc.page_content for doc in docs)

    # Call the LLM with context + user question
    result = chain.invoke({
        "pokemon_entries": entries, 
        "question": question
        })
    print(result)
