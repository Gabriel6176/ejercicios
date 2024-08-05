from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Presupuesto
from ..schemas import PresupuestoModel, PresupuestoCreate  # Asegúrate de tener PresupuestoCreate definido
import logging
from ..schemas import ItemCreate, ItemDisplay  # Asumiendo que tienes estos modelos Pydantic definidos


router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/presupuestos/", response_model=PresupuestoModel)
def create_presupuesto(presupuesto_data: PresupuestoCreate, db: Session = Depends(get_db)):
    logger.info("Creando un nuevo presupuesto...")
    try:
        max_numero = db.query(func.max(Presupuesto.numero)).scalar() or 0
        nuevo_numero = max_numero + 1
        nuevo_presupuesto = Presupuesto(cliente=presupuesto_data.cliente, numero=nuevo_numero)
        db.add(nuevo_presupuesto)
        db.commit()
        db.refresh(nuevo_presupuesto)
        return nuevo_presupuesto
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/items/", response_model=ItemDisplay)
def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    # Verificar si el presupuesto existe
    presupuesto = db.query(Presupuesto).filter(Presupuesto.numero == item_data.numero_presupuesto).first()
    if not presupuesto:
        raise HTTPException(status_code=404, detail="Presupuesto not found")
    # Crear el nuevo item
    item = Item(**item_data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item