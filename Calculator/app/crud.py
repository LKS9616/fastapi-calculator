from sqlalchemy.orm import Session
from . import models, schemas

def create_calculation(db: Session, calc: schemas.CalculationRequest, result: float):
    db_calc = models.Calculation(operation=calc.operation, num1=calc.num1, num2=calc.num2, result=result)
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc

def get_calculations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Calculation).offset(skip).limit(limit).all()