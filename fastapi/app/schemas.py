from pydantic import BaseModel, Field

class PresupuestoModel(BaseModel):
    id: int
    cliente: str
    numero: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "cliente": "Juan Pérez",
                "numero": 1
            }
        }

class PresupuestoCreate(BaseModel):
    cliente: str 

    class Config:
        schema_extra = {
            "example": {
                "cliente": "Juan Pérez"
            }
        }

class ItemCreate(BaseModel):
    tipo: str = Field(..., example="Ventana", description="Tipo de item")
    color: str = Field(..., example="Blanco", description="Color del item")
    ancho: float = Field(..., example=1.5, description="Ancho del item en metros")
    alto: float = Field(..., example=2.0, description="Alto del item en metros")
    revestimiento: str = Field(None, example="Lama", description="Tipo de revestimiento, opcional")
    numero_presupuesto: int = Field(..., example=1, description="Número de presupuesto asociado")

class ItemDisplay(BaseModel):
    id: int
    tipo: str
    color: str
    ancho: float
    alto: float
    revestimiento: str
    numero_presupuesto: int

    class Config:
        orm_mode = True