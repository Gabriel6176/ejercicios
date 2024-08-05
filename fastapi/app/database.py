from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos; usa sqlite para un ejemplo simple y local
DATABASE_URL = "sqlite:///./test.db"

# Crear el motor de la base de datos con la URL de conexión
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Clase base para los modelos declarativos
Base = declarative_base()

# Crear una fábrica de sesiones, vinculada al motor
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos; esta se usará como dependencia en tus rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
