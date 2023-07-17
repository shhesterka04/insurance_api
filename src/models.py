from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rate(Base):
    __tablename__ = "rates"
    rate_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    cargo_type = Column(String, nullable=False)
    rate = Column(String, nullable=False)
