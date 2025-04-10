from fastapi import FastAPI
from routes.route import router as medicine_router

app = FastAPI(title="Medicine Management System")

app.include_router(medicine_router, prefix="/medicines", tags=["Medicines"])
