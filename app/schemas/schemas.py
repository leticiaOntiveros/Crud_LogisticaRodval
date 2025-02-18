from pydantic import BaseModel

class DatosBasicosCreate(BaseModel):
    nombre: str
    descripcion: str

class DatosBasicosResponse(BaseModel):
    ID: int
    nombre: str
    descripcion: str