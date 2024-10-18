from pydantic import BaseModel

class CalculationRequest(BaseModel):
    operation: str
    num1: float
    num2: float

class CalculationResult(BaseModel):
    id: int
    result: float

class Calculation(BaseModel):
    id: int
    operation: str
    num1: float
    num2: float
    result: float

    class Config:
        orm_mode = True