from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def ask_chatbot(query):
    # Initialize the same database and embeddings
    embeddings = OpenAIEmbeddings()
    vector_db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    
    # Setup LLM and Retrieval Chain
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3})
    )
    
    return qa_chain.run(query)