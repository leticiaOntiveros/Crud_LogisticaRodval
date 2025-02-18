from sqlalchemy import Column, Integer, String
from ..database import Base

class Prueba(Base):
    __tablename__ = "prueba"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    precio = Column(String(100))
    stock = Column(String(100))

   