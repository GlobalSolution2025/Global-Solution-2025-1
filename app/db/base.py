from sqlalchemy.ext.declarative import declarative_base

from db.base import Base
from db.models.sensor import SensorData  # Adicione todas as models aqui


Base = declarative_base()
