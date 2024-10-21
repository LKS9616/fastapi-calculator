from pydantic import BaseModel
from typing import Optional, List

class CalculationBase(BaseModel):
    num1: float
    num2: Optional[float] = None
    operator: str

class CalculationCreate(CalculationBase):
    pass

class Calculation(CalculationBase):
    id: int
    result: float

    class Config:
        orm_mode = True

class CalculationResult(BaseModel):
    result: float

class StatisticsInput(BaseModel):
    numbers: List[float]

class StatisticsResult(BaseModel):
    mean: float
    median: float
    standard_deviation: float