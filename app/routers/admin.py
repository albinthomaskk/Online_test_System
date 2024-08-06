from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.dependencies import get_db
from app.dependencies import admin_only

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/tests", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(get_db), current_user: models.User = Depends(admin_only)):
    db_test = models.Test(**test.dict(), created_by=current_user.id)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

@router.post("/tests/{test_id}/questions", response_model=schemas.Question)
def add_question(test_id: int, question: schemas.QuestionCreate, db: Session = Depends(get_db), current_user: models.User = Depends(admin_only)):
    db_question = models.Question(**question.dict(), test_id=test_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@router.get("/results", response_model=List[schemas.UserSubmission])
def view_results(db: Session = Depends(get_db), current_user: models.User = Depends(admin_only)):
    return db.query(models.UserSubmission).all()
