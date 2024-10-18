from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    num1 = Column(Float)
    num2 = Column(Float)
    result = Column(Float)