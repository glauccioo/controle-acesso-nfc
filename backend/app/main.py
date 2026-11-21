from fastapi import FastAPI
from app.database import check_db_connection 
from app.routers.people import router as people_router

app = FastAPI(title="Controle de acesso NFC")

app.include_router(people_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API funcionando"}

@app.get("/db-check")
def database_check():
    check_db_connection()
    return {"status": "ok", "database": "connection"}
