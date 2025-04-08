from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    sqlite_db_name = 'pomodoro.db'
