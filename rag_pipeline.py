from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableMap
from langchain_community.chat_models import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3", base_url="http://localhost:11434")

prompt = PromptTemplate.from_template(
    "Use the context below to answer the question.\n\n{context}\n\nQuestion: {question}"
)

# New LCEL-based stuff chain
rag_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

def query_pdf(pdf_bytes, question):
    from rag_engine.loader import extract_text_from_pdf
    from rag_engine.embedder import embed_and_store, retrieve_relevant_docs

    text = extract_text_from_pdf(pdf_bytes)
    embed_and_store(text)
    relevant_docs = retrieve_relevant_docs(question)

    # use invoke instead of run
    return rag_chain.invoke({"context": relevant_docs, "question": question})
