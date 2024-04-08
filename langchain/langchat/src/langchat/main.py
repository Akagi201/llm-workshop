from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")

llm = ChatCohere()
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are world class technical documentation writer."),
#         ("user", "{input}"),
#     ]
# )
prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}"""
)
document_chain = create_stuff_documents_chain(llm, prompt)
output_parser = StrOutputParser()
docs = loader.load()
embeddings = CohereEmbeddings()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)
chain = prompt | llm | output_parser
answer = chain.invoke({"input": "how can langsmith help with testing?"})
print(answer)
