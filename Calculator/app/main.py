from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .calculator import calculate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_model=schemas.CalculationResult)
async def calculate_api(calc_request: schemas.CalculationRequest, db: Session = Depends(get_db)):
    try:
        result = calculate(calc_request.operation, calc_request.num1, calc_request.num2)
        db_calc = crud.create_calculation(db, calc_request, result)
        return schemas.CalculationResult(id=db_calc.id, result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@app.get("/calculations", response_model=list[schemas.Calculation])
async def read_calculations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    calculations = crud.get_calculations(db, skip=skip, limit=limit)
    return calculations