from pydantic import BaseModel
from typing import Literal, List

class ProblemOut(BaseModel):
    slug: str
    title: str
    difficulty: Literal["easy","medium","hard"]
    statement_md: str
    starter_code_py: str
    starter_code_java: str
    class Config:
        from_attributes = True

class SubmitIn(BaseModel):
    slug: str
    language: Literal["python","java"]
    code: str

class VerdictOut(BaseModel):
    passed: bool
    tests_total: int
    tests_passed: int
    details: List[str]
