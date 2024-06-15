from typing import Union

from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    description: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    ecommerce_id: int

    class Config:
        orm_mode = True


class EcommerceBase(BaseModel):
    name: str


class EcommerceCreate(EcommerceBase):
    pass


class Ecommerce(EcommerceBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True


class MessageBase(BaseModel):
    customer_name: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True


class ReplyBase(BaseModel):
    sender: str
    content: str
    date_created: datetime = datetime.now()


class ReplyCreate(ReplyBase):
    pass


class Reply(ReplyBase):
    id: int
    message_id: int

    class Config:
        orm_mode = True