from pydantic import BaseModel

class Settings(BaseModel):
    DB_HOST: str = '127.0.0.1'
    DB_PORT: str = '5432'
    DB_NAME: str = 'pomodorodb'
    ACC_PASSWORD: str = 'ma20ks08im'
    ACC_NAME: str = 'pydevaz'
    DB_ENGINE: str = 'postgresql+psycopg2'

    @property
    def db_url(self):
        return f'{self.DB_ENGINE}://{self.ACC_NAME}:{self.ACC_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'