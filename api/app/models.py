from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    difficulty = Column(String, default="easy")
    statement_md = Column(Text, nullable=False)
    starter_code_py = Column(Text, default="")
    starter_code_java = Column(Text, default="")
    test_cases = relationship("TestCase", back_populates="problem", cascade="all, delete-orphan")

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="CASCADE"))
    input = Column(Text, nullable=False)
    output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=True)
    problem = relationship("Problem", back_populates="test_cases")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    language = Column(String)
    code = Column(Text)
    verdict = Column(String)
    time_ms = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
