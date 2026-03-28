# 🤖 My First LangChain AI Agent

A conversational AI agent built with LangChain + Groq that can reason, 
use tools, and answer questions interactively.

## 🛠️ Tech Stack

- **LangChain** — Agent framework (ReAct pattern)
- **Groq API** — LLM (llama-3.3-70b-versatile) — free & fast
- **LangSmith** — Tracing & monitoring
- **Python** — Core language

## 🧰 Tools the Agent Can Use

| Tool | Description | Example |
|------|-------------|---------|
| `calculator` | Solves any math expression | `15% of 2500` |
| `word_length` | Counts characters in text | `'Machine Learning'` |
| `reverse_text` | Reverses any string | `'LangChain'` |

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/marisha119-AI/LangChain_Agent
cd my-agent

### 2. Install dependencies
pip install langchain langchain-groq langchain-classic python-dotenv

### 3. Set up environment variables
Create a `.env` file:
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=my-agent

### 4. Run the agent
python agent.py

## 💡 How it Works

The agent uses the **ReAct (Reasoning + Acting)** pattern:

User Question
      ↓
LLM thinks — which tool to use?
      ↓
Calls the tool
      ↓
Gets result back
      ↓
LLM decides — final answer or need another tool?
      ↓
Final Answer

## 📊 LangSmith Tracing

All agent runs are automatically traced on LangSmith dashboard — 
you can see exactly which tools were called, 
how long each step took, and the full reasoning chain.

## 🔮 Next Steps

- [ ] Add web search tool (Tavily)
- [ ] Add memory (multi-turn conversation)
- [ ] Build a frontend with Streamlit
- [ ] Deploy to cloud

## 📚 What I Learned

- How LLMs work (tokenization, embeddings, attention mechanism)
- ReAct agent pattern — Reasoning + Acting
- How to build and connect custom tools to an LLM
- How to trace and monitor AI agents with LangSmith
