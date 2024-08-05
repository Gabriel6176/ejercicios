from fastapi import FastAPI
from .routers.presupuesto_router import router as presupuesto_router
from .database import engine
from .models import Base

# Crear la instancia de FastAPI
app = FastAPI()

# Incluir los routers en la aplicación
app.include_router(presupuesto_router)




