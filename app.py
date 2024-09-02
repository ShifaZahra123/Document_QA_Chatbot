import streamlit as st
import os
from langchain_groq import ChatGroq # for Chatbot
from langchain.text_splitter import RecursiveCharacterTextSplitter # Convert text into Chunks
from langchain.chains.combine_documents import create_stuff_documents_chain # To get relevenat document Q/A for building and setting up context
from langchain_core.prompts import ChatPromptTemplate # For creating own customize Chatbot
from langchain.chains import create_retrieval_chain  
from langchain_community.vectorstores import FAISS  # Vector store DB created by Facebook doing Similarity Search
from langchain_community.document_loaders import PyPDFDirectoryLoader # Read PDF Files
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Provide Embeddings by Google by using Google API Keys, Vector Embedding Technique (Convert Chunks of Text to Vectors)
from dotenv import load_dotenv
import os
load_dotenv()   ## FOR LOADING ENVIRONMENT VARIABLES

## load the GROQ And GOOGLE API KEY key from .env variable
groq_api_key=os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

st.title("Document Q & A Bot")

## Gema Model is using for this ChatBot Model: Gemma-7b-It
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}  ## Context
<context>
Questions:{input}  ## input for llm

"""
)

def vector_embedding():  ## Read pdf file, Convert into chunks, apply Google Generative AI Embeddings, Store in VectoreStore DB (FAISS) AND KEEP IT IN SESSION STAE so i can use it anywhere i want to use

    if "vectors" not in st.session_state:

        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001") ## Google model for embedding
        st.session_state.loader=PyPDFDirectoryLoader("./Latest_Research_Paper") ## Data Ingestion
        st.session_state.docs=st.session_state.loader.load() ## Document Loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200) ## Chunk Creation, chunk_overlap is used so that nothing will be missed
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20]) #splitting
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings) #vector Google Generative embeddings





prompt1=st.text_input("Enter Your Question From Documents")


if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")

import time



if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever() ## as_retriever() function: Create Interface and Provide info. to end-user, Retreive information from Vectore DB(FAISS) 
    retrieval_chain=create_retrieval_chain(retriever,document_chain) ## Run in form of Chain
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1}) ## invoke function: whatever input i given in this prompt, it should able to retreive response from entire chain
    print("Response time :",time.process_time()-start) ## Get Total Response Time
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content) 
            st.write("--------------------------------")
