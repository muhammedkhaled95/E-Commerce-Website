from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text, VARCHAR
from sqlalchemy.orm import relationship
from database.database import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    role = Column(String, nullable=False)

    carts = relationship("Cart", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    orders = relationship("Order", back_populates="user")
    addresses = relationship("Address", back_populates="user")

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, default=0.0)
    status = Column(String, default="open")  # E.g., open, completed

    user = relationship("User", back_populates="carts")
    cart_items = relationship("CartItem", back_populates="cart")
    payments = relationship("Payment", back_populates="cart")
    orders = relationship("Order", back_populates="cart")

class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float)

    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    discount_percentage = Column(Float, default=0.0)
    rating = Column(Float)
    stock = Column(Integer, default=0)
    brand = Column(String)
    thumbnail = Column(String)
    images = Column(String)  # Assuming it's a comma-separated list of image URLs
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    cart_id = Column(Integer, ForeignKey('carts.id'))
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # E.g., pending, completed, failed
    payment_method = Column(String, nullable=False)
    transaction_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="payments")
    cart = relationship("Cart", back_populates="payments")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    cart_id = Column(Integer, ForeignKey('carts.id'))
    total_amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # E.g., pending, shipped, delivered
    shipping_address = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="orders")
    cart = relationship("Cart", back_populates="orders")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String, nullable=False)  # E.g., shipping, billing
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=True)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="addresses")
