from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Ecommerce(Base):
    __tablename__ = "ecommerces"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="ecommerce")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(Integer)
    description = Column(String)
    ecommerce_id = Column(Integer, ForeignKey("ecommerces.id"))

    ecommerce = relationship("Ecommerce", back_populates="products")
    messages = relationship("Message", back_populates="product")


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))

    replies = relationship("Reply", back_populates="message")
    product = relationship("Product", back_populates="messages")


class Reply(Base):
    __tablename__ = "replies"
    id = Column(Integer, primary_key=True)
    sender = Column(String, index=True)
    content = Column(String)
    created_at = Column(String)
    message_id = Column(Integer, ForeignKey("messages.id"))

    message = relationship("Message", back_populates="replies")
