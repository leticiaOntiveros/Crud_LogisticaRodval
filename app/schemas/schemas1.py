from pydantic import BaseModel

class PruebaCreate(BaseModel):
    nombre: str
    precio: str
    stock: str

class PruebaResponse(BaseModel):
    id: int
    nombre: str
    precio: str
    stock: str