from sqlalchemy import Column, Boolean, Float, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

import datetime

Base = declarative_base() # Create a base class for the models

class User(Base):
    __tablename__ = 'user' # Name of the table in the database

    user_id = Column(Integer, primary_key=True) # Primary key column
    user_name = Column(String) # Name column
    user_email = Column(String, unique=True) # Email column
    user_password = Column(String) # Password column
    created_at = Column(DateTime, default=datetime.datetime.utcnow) # Timestamp column for when the user was created

class Product(Base):
    __tablename__ = 'product' # Name of the table in the database

    user_id = Column(Integer, ForeignKey('user.user_id')) # Foreign key column to link to the User table
    product_id = Column(Integer, primary_key=True) # Primary key column
    product_name = Column(String) # Name column
    product_description = Column(String) # Description column for the product
    product_budget = Column(Float) # The user's budget for the product
    product_price_tolerance = Column(Float) # The user's price tolerance for the product
    product_currency = Column(String) # The user's currency for the product price
    created_at = Column(DateTime, default=datetime.datetime.utcnow) # Timestamp column for when the product was created
    is_active = Column(Boolean, default=True) # Column to indicate if the product is active (1) or not (0)
    owner = relationship("User") # Relationship to the User model

class PriceHistory(Base):
    __tablename__ = 'price_history' # Name of the table in the database

    price_history_id = Column(Integer, primary_key=True) # Primary key column
    product_id = Column(Integer, ForeignKey('product.product_id')) # Foreign key column to link to the Product table
    price_found = Column(Float) # The price of the product at a specific time
    platform_found = Column(String) # The platform where the price was found (e.g., Amazon, eBay)
    url_found = Column(String) # The URL where the price was found
    currency_found = Column(String) # The currency of the price found
    found_at = Column(DateTime, default=datetime.datetime.utcnow) # Timestamp column for when the price was recorded
    owner = relationship("Product") # Relationship to the Product model