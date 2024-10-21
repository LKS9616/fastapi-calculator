from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    num1 = Column(Float)
    num2 = Column(Float)
    operator = Column(String)
    result = Column(Float)