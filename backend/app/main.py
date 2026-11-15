from fastapi import FastAPI

app = FastAPI(title="controle de acesso NFC")

@app.get("/health")
def health_check():
    return {"status": "ok", "messsage": "API funcionando"}