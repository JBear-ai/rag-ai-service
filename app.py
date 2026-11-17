from fastapi import FastAPI

app = FastAPI(title="Board RAG AI Service")

@app.get("/health")
def health():
    return {"status": "OK"}