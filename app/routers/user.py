from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models, utils
from app.dependencies import get_current_user, get_db

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/tests", response_model=List[schemas.Test])
def list_tests(db: Session = Depends(get_db)):
    return db.query(models.Test).all()

@router.post("/submit", response_model=schemas.UserSubmission)
def submit_test(submission: schemas.TestSubmission, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_submission = utils.evaluate_submission(submission, current_user.id, db)
    return db_submission

@router.get("/results", response_model=List[schemas.UserSubmission])
def view_results(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.UserSubmission).filter(models.UserSubmission.user_id == current_user.id).all()
