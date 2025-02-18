from sqlalchemy import Column, Integer, String
from ..database import Base

class DatosBasicos(Base):
    __tablename__ = "datosBasicos"

    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    descripcion = Column(String(100))

   