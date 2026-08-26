from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB, EventoDB
from schemas import ProdutoCreate, ProdutoResponse, EventoCreate, EventoResponse
from fastapi.middleware.cors import CORSMiddleware#<--criar a tabela se não existe 

app = FastAPI()

@app.on_event("startup")
def criar_tabelas():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
 CORSMiddleware,
 allow_origins=['*'],
 allow_methods=['*'],
 allow_headers=['*'],
)

def buscar_produto(db: Session, produto_id: int):
    return db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()

@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = buscar_produto(db, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto

@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = buscar_produto(db, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto

@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = buscar_produto(db, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()




@app.get('/eventos', response_model=list[EventoResponse])
def listar_eventos(db: Session = Depends(get_db)):
  return db.query(EventoDB).all()   


@app.post('/eventos', response_model=EventoResponse, status_code=201)
def criar_evento(evento: EventoCreate, db: Session = Depends(get_db)):
   novo_evento = EventoDB(**evento.dict())
   db.add(novo_evento)
   db.commit()
   db.refresh(novo_evento)
   return novo_evento


@app.get('/eventos/{evento_id}', response_model=EventoResponse)
def obter_evento(evento_id: int, db: Session = Depends(get_db)):
  evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
  if evento is None:
    raise HTTPException(status_code=404, detail='Evento não encontrado')
  return evento


@app.delete('/eventos/{evento_id}', status_code=204)
def remover_evento(evento_id: int, db: Session = Depends(get_db)): 
   evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
   if evento is None:
    raise HTTPException(status_code=404, detail='Evento não encontrado')
   

   db.delete(evento)
   db.commit()


@app.put('/eventos/{evento_id}', response_model=EventoResponse)
def atualizar_evento(evento_id: int, dados: EventoCreate, db:
Session = Depends(get_db)):
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
    if evento is None:
     raise HTTPException(status_code=404, detail='Evento não encontrado')
 
    evento.nome = dados.nome
    evento.local = dados.local
    evento.horario = dados.horario
    db.commit()
    db.refresh(evento)
    return