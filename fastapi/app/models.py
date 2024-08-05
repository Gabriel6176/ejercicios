# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Presupuesto(Base):
    __tablename__ = 'presupuesto'
    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, index=True, nullable=True)  # Cliente es opcional
    numero = Column(Integer, index=True, unique=True)  # No autoincrementable
    items = relationship("Item", back_populates="presupuesto")

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    color = Column(String)
    ancho = Column(Float)
    alto = Column(Float)
    revestimiento = Column(String)
    numero_presupuesto = Column(Integer, ForeignKey('presupuesto.numero'))  # Actualización de la FK
    presupuesto = relationship("Presupuesto", back_populates="items") 

    



