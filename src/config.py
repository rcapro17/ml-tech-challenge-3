from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # 1. REMOVA os valores default inseguros ("localhost", "mlpass", etc.)
    # Isso FORÇA o Pydantic a ler os valores das variáveis de ambiente no Render.
    # Se a variável não for encontrada, o deploy falhará (o que é o desejado).
    DB_HOST: str
    DB_PORT: int = 5432 # A porta 5432 é o padrão, pode manter o default
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    
    TZ: str = "America/Sao_Paulo"

    @property
    def database_url(self) -> str:
        # A URL é construída com variáveis lidas do ambiente do Render
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()