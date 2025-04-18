# 🧠 Pokémon Advisor – AI-Powered Pokédex Q&A

**Pokémon Advisor** is an intelligent agent that uses vector search and a local LLM to answer natural language questions about Generation 1 Pokémon.

### 🔍 How it works:

- 🧾 Loads a structured Pokémon dataset (stats like HP, Attack, Defense, Speed, Type, etc.)
- 🧠 Uses **ChromaDB** to create a vector store of Pokémon descriptions
- 🔗 Employs **LangChain** to retrieve relevant Pokémon entries based on the user's question
- 🤖 Powered by **Ollama's llama3.2** model to generate thoughtful, context-aware responses



---

## 🚀 How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/Pokemon-Advisor.git
cd Pokemon-Advisor
```

2. **Install the required dependencies**
Make sure you have Python 3.10+ installed. Then install dependencies:
```bash
pip install -r requirements.txt
```

3. **Run the Agent**
```bash
python main.py
```

## ⚡ Example Output

Question: Who would win: Charizard or Blastoise?

Output:
A classic battle between two of the most iconic Generation 1 Pokémon!

To determine who would win, let's analyze the stats:

Charizard
HP: 78
Attack: 84
Defense: 78
Special Attack: 109
Special Defense: 85
Speed: 100

Blastoise
HP: 79
Attack: 83
Defense: 100
Special Attack: 85
Special Defense: 105
Speed: 78

Considering the stats, Charizard has a slight advantage due to its higher Special Attack and Speed. However, Blastoise’s strong Defense and Water-type advantage make this a very close and strategic battle!



