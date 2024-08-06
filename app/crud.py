from sqlalchemy.orm import Session
from app import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_test(db: Session, test: schemas.TestCreate, user_id: int):
    db_test = models.Test(**test.dict(), created_by=user_id)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def add_question(db: Session, question: schemas.QuestionCreate, test_id: int):
    db_question = models.Question(**question.dict(), test_id=test_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_tests(db: Session):
    return db.query(models.Test).all()
