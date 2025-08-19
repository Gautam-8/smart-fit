from fastapi import APIRouter, UploadFile

from routes.rag_pipe import Rag_pipe



router = APIRouter()

# POST /chat/ask - Send question, get RAG-powered response
# GET /chat/history/{user_id} - Get chat history

@router.get("/chat/ask")
def ask(query: str):
    rp = Rag_pipe()
    res = rp.retrieve(query)
    return res

@router.post("/upload_kb")
def upload_kb(file: UploadFile):
    rp = Rag_pipe()
    rp.uploadfile(file)
    return {
        "message" : "updated"
    }

