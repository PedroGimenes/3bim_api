<<<<<<< HEAD
=======
# models.py
>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProdutoDB(Base):
<<<<<<< HEAD
 
  __tablename__ = 'produtos'

  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String(100), nullable=False)
  preco = Column(Float, nullable=False)
  quantidade = Column(Integer, nullable=False)
=======
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
>>>>>>> 14d06886dc54d91a5e1442d089da045973f50cfe
