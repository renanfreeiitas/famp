from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configuracoes gerais usadas na aplicacao.
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://admin:password@localhost:5432/faculdade"
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensite = True
         

settings = Settings()
    
    