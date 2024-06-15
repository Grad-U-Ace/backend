from sqlalchemy.orm import Session

from sql import models, schemas


def get_ecommerces(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ecommerce).offset(skip).limit(limit).all()


def get_ecommerce_by_name(db: Session, name: str):
    return db.query(models.Ecommerce).filter(models.Ecommerce.name == name).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products_by_ecommerce_id(db: Session, ecommerce_id: int):
    return db.query(models.Product).filter(models.Product.ecommerce_id == ecommerce_id).first()


def get_products_by_product_name(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.name == product_name).first()


def get_message_by_name(db: Session, message_customer_name: str):
    return db.query(models.Message).filter(models.Message.customer_name == message_customer_name).first()


def get_message_by_id(db: Session, message_id: int):
    return db.query(models.Message).filter(models.Message.id == message_id).first()


def get_reply_by_id(db: Session, reply_id: int):
    return db.query(models.Reply).filter(models.Reply.id == reply_id).first()

def create_ecommerce(db: Session, ecommerce: schemas.EcommerceCreate):
    db_ecommerce = models.Ecommerce(**ecommerce.dict())
    db.add(db_ecommerce)
    db.commit()
    db.refresh(db_ecommerce)
    return db_ecommerce


def create_product(db: Session, product: schemas.ProductCreate, ecommerce_name: str):
    db_ecommerce = db.query(models.Ecommerce).filter(models.Ecommerce.name == ecommerce_name).first()
    db_product = models.Product(**product.dict(), ecommerce_id=db_ecommerce.id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def create_message(db: Session, message: schemas.MessageCreate, product_id: int):
    db_message = models.Message(**message.dict(), product_id=product_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def create_reply(db: Session, reply: schemas.ReplyCreate, message_id: int):
    db_reply = models.Reply(**reply.dict(), message_id=message_id)
    db.add(db_reply)
    db.commit()
    db.refresh(db_reply)
    return db_reply