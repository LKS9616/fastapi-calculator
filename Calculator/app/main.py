from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from .database import SessionLocal, engine
import math
import statistics

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/calculate/", response_model=schemas.CalculationResult)
def calculate(calculation: schemas.CalculationCreate, db: Session = Depends(get_db)):
    if calculation.operator not in ['+', '-', '*', '/', 'inv', 'sqrt']:
        raise HTTPException(status_code=400, detail="잘못된 연산자입니다. '+', '-', '*', '/', 'inv', 'sqrt' 중 하나를 사용하세요.")
    
    result = None
    if calculation.operator == '+':
        result = calculation.num1 + calculation.num2
    elif calculation.operator == '-':
        result = calculation.num1 - calculation.num2
    elif calculation.operator == '*':
        result = calculation.num1 * calculation.num2
    elif calculation.operator == '/':
        if calculation.num2 == 0:
            raise HTTPException(status_code=400, detail="0으로 나눌 수 없습니다.")
        result = calculation.num1 / calculation.num2
    elif calculation.operator == 'inv':
        if calculation.num1 == 0:
            raise HTTPException(status_code=400, detail="0의 역수는 정의되지 않습니다.")
        result = 1 / calculation.num1
    elif calculation.operator == 'sqrt':
        if calculation.num1 < 0:
            raise HTTPException(status_code=400, detail="음수의 제곱근은 실수 범위에서 정의되지 않습니다.")
        result = math.sqrt(calculation.num1)
    
    db_calculation = models.Calculation(num1=calculation.num1, num2=calculation.num2, operator=calculation.operator, result=result)
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation

@app.post("/statistics/", response_model=schemas.StatisticsResult)
def calculate_statistics(data: schemas.StatisticsInput):
    if len(data.numbers) == 0:
        raise HTTPException(status_code=400, detail="데이터가 비어있습니다.")
    
    mean = statistics.mean(data.numbers)
    median = statistics.median(data.numbers)
    stdev = statistics.stdev(data.numbers) if len(data.numbers) > 1 else 0
    
    return {"mean": mean, "median": median, "standard_deviation": stdev}