import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub

# Load environment variables
load_dotenv()

# Initialize LLM via Groq (free & very fast!)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# Tool 1: Calculator
@tool
def calculator(expression: str) -> str:
    """
    Calculates any math expression.
    Example input: '144 ** 0.5' or '100 / 4 + 50'
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Tool 2: Word length
@tool
def word_length(word: str) -> str:
    """
    Returns the number of characters in a word or sentence.
    Example input: 'langchain'
    """
    return f"The word '{word}' has {len(word)} characters."

# Tool 3: Reverse text
@tool
def reverse_text(text: str) -> str:
    """
    Reverses any given text.
    Example input: 'hello'
    """
    return f"Reversed text: {text[::-1]}"

# All tools in a list
tools = [calculator, word_length, reverse_text]

# Load ReAct prompt and build agent
print("Loading agent...")
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)

# Test questions
print("\n" + "=" * 50)
print("Agent is running!")
print("=" * 50 + "\n")

questions = [
    "What is the square root of 144?",
    "How many characters are in the word 'artificial intelligence'?",
    "Reverse the text 'LangChain'."
]

for question in questions:
    print(f"\nQuestion: {question}")
    print("-" * 40)
    result = agent_executor.invoke({"input": question})
    print(f"\nFinal Answer: {result['output']}")
    print("=" * 50)