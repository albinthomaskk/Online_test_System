from sqlalchemy import Column, Integer, String, Enum
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum("admin", "user", name="role"))

class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_by = Column(Integer)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer)
    question_text = Column(String)

class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    answer_text = Column(String)
    is_correct = Column(Integer)

class UserSubmission(Base):
    __tablename__ = "user_submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    test_id = Column(Integer)
    submission_time = Column(String)
    score = Column(Integer)

class UserAnswer(Base):
    __tablename__ = "user_answers"
    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer)
    question_id = Column(Integer)
    selected_answer = Column(Integer)
