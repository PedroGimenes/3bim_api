<<<<<<< HEAD
from pydantic import BaseModel

class ProdutoBase(BaseModel):
 
  nome: str
  preco: float
  quantidade: int

class ProdutoCreate(ProdutoBase):
  pass

class ProdutoResponse(ProdutoBase):
  id: int

class Config:
  from_attributes = True
=======
# schemas.py
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int
class ProdutoCreate(ProdutoBase):
    pass
class ProdutoResponse(ProdutoBase):
    id: int
class Config:
    from_attributes = True
>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
