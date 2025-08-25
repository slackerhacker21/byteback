from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .db import SessionLocal, init_db
from . import models
from .schemas import ProblemOut, SubmitIn, VerdictOut
from .judge import Judge
from sqlalchemy import select
import os

init_db()

app = FastAPI(title="ByteBack API", version="0.1")

origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/problems", response_model=list[ProblemOut])
def list_problems():
    with SessionLocal() as db:
        rows = db.execute(select(models.Problem)).scalars().all()
        return rows

@app.get("/problems/{slug}", response_model=ProblemOut)
def get_problem(slug: str):
    with SessionLocal() as db:
        p = db.execute(select(models.Problem).where(models.Problem.slug == slug)).scalar_one_or_none()
        if not p:
            raise HTTPException(404, "problem not found")
        return p

@app.post("/submit", response_model=VerdictOut)
async def submit(payload: SubmitIn):
    with SessionLocal() as db:
        p = db.execute(select(models.Problem).where(models.Problem.slug == payload.slug)).scalar_one_or_none()
        if not p:
            raise HTTPException(404, "problem not found")
        tcs = p.test_cases
    total = len(tcs)
    passed = 0
    details: list[str] = []
    for idx, tc in enumerate(tcs, start=1):
        stdout, time_ms = await Judge.run(payload.language, payload.code, tc.input)
        ok = stdout.strip() == tc.output.strip()
        passed += int(ok)
        details.append(f"TC{idx}: {'OK' if ok else 'WA'}")
    return VerdictOut(passed=(passed == total), tests_total=total, tests_passed=passed, details=details)
