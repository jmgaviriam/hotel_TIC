from fastapi import FastAPI,HTTPException
import db

api=FastAPI()

@api.get("/reservas")
async def obtener_ocupacion():
    return db.obtener_lista_reservas()

@api.post("/reservas/crear")
async def crear_reserva(reserva: db.reservas):
    reserva_exitosa = db.crear_reserva(reserva)
    if reserva_exitosa:
        return{"Mensaje": "Reservación creada con éxito"}
    else:
        raise HTTPException(status_code=400, detail="No se pudo realziar la reservación")