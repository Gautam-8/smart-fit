from fastapi import UploadFile
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model
from langchain import hub
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


class Rag_pipe:
    def __init__(self):
        self.textsplitter = RecursiveCharacterTextSplitter( chunk_size=500, chunk_overlap=100)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        self.vector_db = None

    def uploadfile(self, file: UploadFile):
        docs = PyMuPDFLoader(file).load()
        chunks = self.textsplitter.split_documents(docs)
        self.vector_db = FAISS.from_documents(chunks, self.embeddings)

    def retrieve(self, query: str):
        llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
        retriever = self.vector_db.as_retriever(search_type="similarity", search_kwargs={'k': 3})
        docs = retriever.invoke(query)
        
        prompt = {
            "question" : "You are fitness expert answer user query : {query} from given context only if not available just not updated",
            "context" : docs 
        }

        res  = llm.invoke(prompt)
        return res




