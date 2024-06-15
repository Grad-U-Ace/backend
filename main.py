from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post("/ecommerce/{ecommerce_name}/product/", response_model=schemas.Product)
def create_product(ecommerce_name: str, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_products_by_product_name(db, product_name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already registered")

    return crud.create_product(db=db, product=product, ecommerce_name=ecommerce_name)

@app.post("/ecommerce/{ecommerce_name}/product/{product_id}/message/", response_model=schemas.Message)
def create_message(product_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = crud.get_message_by_name(db, message_customer_name=message.customer_name)
    if db_message:
        raise HTTPException(status_code=400, detail="User already registered")

    return crud.create_message(db=db, message=message, product_id=product_id)


@app.post("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}/reply", response_model=schemas.Reply)
def create_reply(message_id: int, reply: schemas.ReplyCreate, db: Session = Depends(get_db)):
    return crud.create_reply(db=db, reply=reply, message_id=message_id)


# - intelligent agent
@app.get("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}/reply/{reply_id}/ask")
def ask_for_answer(reply_id: int, db: Session = Depends(get_db)):
    reply = crud.get_reply_by_id(db=db, reply_id=reply_id)
    if reply:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"What is the proper answer to this question? {reply.content}"},
            ]
        )

        return completion.choices[0].message
    else:
        raise HTTPException(status_code=404, detail="Reply not found")

# - support multi language
@app.get("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}/reply/{reply_id}/translate")
def ask_for_translation(reply_id: int, db: Session = Depends(get_db)):
    reply = crud.get_reply_by_id(db=db, reply_id=reply_id)
    if reply:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Translate the following sentences to Bahasa Indonesia"},
                {"role": "user", "content": f"{reply.content}"},
            ]
        )

        return completion.choices[0].message
    else:
        raise HTTPException(status_code=404, detail="Reply not found")

# - summarize conv
@app.get("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}/summarize")
def ask_for_summary(message_id: int, db: Session = Depends(get_db)):
    message = crud.get_message_by_id(db=db, message_id=message_id)
    print([reply.__dict__['content'] for reply in message.replies])
    if message:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following conversation."},
                {"role": "user", "content": f"{[reply.__dict__['content'] for reply in message.replies]}"},
            ]
        )

        return completion.choices[0].message
    else:
        raise HTTPException(status_code=404, detail="Reply not found")

# - sentiment analysis
@app.get("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}/reply/{reply_id}/sentiment")
def ask_for_sentiment(reply_id: int, db: Session = Depends(get_db)):
    reply = crud.get_reply_by_id(db=db, reply_id=reply_id)
    if reply:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "For every prompt that you are given, gives a sentiment analysis for the sentences given. Answer with only one word between neutral, positive, or negative. "},
                {"role": "user", "content": f"{reply.content}"},
            ]
        )

        return completion.choices[0].message
    else:
        raise HTTPException(status_code=404, detail="Reply not found")


# - conversation tagging
@app.put("/ecommerce/{ecommerce_name}/product/{product_id}/message/{message_id}", response_model=schemas.Message)
def change_message_tag(message_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.update_message(db=db, message=message, message_id=message_id)

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
