from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy.orm import Session

import data
from sql import models, schemas, crud
from sql.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

load_dotenv()
app = FastAPI()
client = OpenAI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ecommerce/", response_model=list[schemas.Ecommerce])
def read_all_ecommerce(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ecommerces = crud.get_ecommerces(db, skip=skip, limit=limit)
    return ecommerces


@app.get("/ecommerce/{ecommerce_name}/", response_model=list[schemas.Ecommerce])
def read_ecommerce_by_name(ecommerce_name: str, db: Session = Depends(get_db)):
    ecommerces = crud.get_ecommerce_by_name(db, name=ecommerce_name)
    return ecommerces

@app.post("/ecommerce/", response_model=schemas.Ecommerce)
def create_ecommerce(ecommerce: schemas.EcommerceCreate, db: Session = Depends(get_db)):
    db_ecommerce = crud.get_ecommerce_by_name(db, name=ecommerce.name)
    if db_ecommerce:
        raise HTTPException(status_code=400, detail="Ecommerce platform already registered")
    return crud.create_ecommerce(db=db, ecommerce=ecommerce)


@app.post("/ecommerce/{ecommerce_name}/product", response_model=schemas.Ecommerce)
def create_product(ecommerce_name: str, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_ecommerce(db=db, product=product, ecommerce=ecommerce_name)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chat")
def answer():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of the United States?"},
        ]
    )
    return completion.choices[0].message


@app.post("/")
def generate_answer():
    """
    Should receive message and product detail
    :return:
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of the United States?"},
        ]
    )
    return completion.choices[0].message
