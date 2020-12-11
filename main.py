from fastapi import FastAPI,HTTPException
import db

api = FastAPI()

@api.get("/reservas")
async def obtener_ocupacion():
    return db.obtener_lista_reservas()