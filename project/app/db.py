import os
from databases import Database
from sqlalchemy.dialects.postgresql import JSON, ARRAY, BYTEA
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Unicode, String, create_engine, DateTime, Table, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from sqlalchemy.sql import func


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, unique=True)
    name = Column(Text, unique=True,index=True)

# databases query builder
database = Database(DATABASE_URL)