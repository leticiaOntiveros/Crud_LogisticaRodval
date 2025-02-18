from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import DatosBasicos
from app.schemas.schemas import DatosBasicosCreate, DatosBasicosResponse
from app.models.models1 import Prueba  # Importa el modelo prueba
from app.schemas.schemas1 import PruebaCreate, PruebaResponse
from app.database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo registro en datosBasicos
@router.post("/datos-basicos/", response_model=DatosBasicosResponse)
def create_datos_basicos(datos: DatosBasicosCreate, db: Session = Depends(get_db)):
    db_datos = DatosBasicos(**datos.dict())  # Usa el modelo DatosBasicos
    db.add(db_datos)
    db.commit()
    db.refresh(db_datos)
    return db_datos

# Obtener un registro por ID
@router.get("/datos-basicos/{datos_id}", response_model=DatosBasicosResponse)
def read_datos_basicos(datos_id: int, db: Session = Depends(get_db)):
    datos = db.query(DatosBasicos).filter(DatosBasicos.id == datos_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return datos

# Crear un nuevo registro en la tabla de prueba
@router.post("/prueba/", response_model=PruebaResponse)
def create_prueba(datos: PruebaCreate, db: Session = Depends(get_db)):
    db_datos = Prueba(**datos.dict())  # Usa el modelo DatosBasicos
    db.add(db_datos)
    db.commit()
    db.refresh(db_datos)
    return db_datos

# Obtener un registro por id en la tabla de prueba
@router.get("/prueba/{datos_id}", response_model=PruebaResponse)
def read_prueba(datos_id: int, db: Session = Depends(get_db)):
    datos = db.query(Prueba).filter(Prueba.id == datos_id).first()
    if datos is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return datos