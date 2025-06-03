from fastapi import FastAPI
from api.routes import sensor

app = FastAPI()

app.include_router(sensor.router)
