from fastapi import FastAPI
from app.core.config import settings
from app.api import health, users, skills ,skill_history,analysis, recommendations

from app.core.logging import setup_logging
from app.core.exceptions import global_exception_handler
from fastapi import Request
import logging
from app.db.database import check_db_connection 

# 1️⃣ Setup logging FIRST
setup_logging()

# 2️⃣ Create logger
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(skills.router)
app.include_router(skill_history.router)
app.include_router(analysis.router)
app.include_router(recommendations.router)

@app.on_event("startup")
def startup_event():
    logger.info("SkillRot backend starting up...")
    check_db_connection()

@app.on_event("shutdown")
def shutdown_event():
    logger.info("SkillRot backend shutting down...")


@app.get("/")
def root():
    return {"message": "SkillRot backend running with Render DB"}
