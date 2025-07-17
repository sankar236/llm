from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rag_engine.rag_pipeline import query_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def ask_question(file: UploadFile = File(...), question: str = ""):
    content = await file.read()
    answer = query_pdf(content, question)
    return {"answer": answer}