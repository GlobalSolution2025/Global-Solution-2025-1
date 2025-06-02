from typing import Union

from fastapi import FastAPI
from api.endpoints import router

app = FastAPI()

# Inclui os endpoints do módulo
app.include_router(router)
