import langwatch.langchain
from langchain.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere

# Create your LangChain
model = ChatCohere()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model

# Use the tracer context manager
with langwatch.langchain.LangChainTracer(
    metadata={
        "user_id": "optional-user-123",
        "thread_id": "optional-thread-456",
    }
) as langWatchCallback:
    # Invoke LangChain with LangWatch callbacks
    result = chain.invoke({"topic": "bears"}, config={"callbacks": [langWatchCallback]})
