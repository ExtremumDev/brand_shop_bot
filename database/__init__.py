from .database import DataBase

from config import settings


db = DataBase(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    db_name=settings.DB_NAME,
    user=settings.DB_USER,
    password=settings.DB_PASSWORD
)
