"""
Configuración de la Base de Datos de Entrenamiento.
Carga variables de entorno desde .env mediante python-dotenv.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

class DatabaseConfig:
    HOST: str = os.getenv("DB_HOST", "localhost")
    PORT: int = int(os.getenv("DB_PORT", "5432"))
    NAME: str = os.getenv("DB_NAME", "db_dataset_valuo")
    USER: str = os.getenv("DB_USER", "postgres")
    PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
    SCHEMA: str = os.getenv("DB_SCHEMA", "public")
    POOL_SIZE: int = int(os.getenv("DB_POOL_SIZE", "5"))
    MAX_OVERFLOW: int = int(os.getenv("DB_MAX_OVERFLOW", "10"))
    SSLMODE: str = os.getenv("DB_SSLMODE", "prefer")

    @classmethod
    def get_sqlalchemy_url(cls, dbname: str = None, db_name: str = None) -> str:
        target_db = dbname or db_name or cls.NAME
        from urllib.parse import quote_plus
        user_enc = quote_plus(cls.USER)
        pass_enc = quote_plus(cls.PASSWORD)
        url = f"postgresql+psycopg2://{user_enc}:{pass_enc}@{cls.HOST}:{cls.PORT}/{target_db}"
        if cls.SSLMODE:
            url += f"?sslmode={cls.SSLMODE}"
        return url

    @classmethod
    def get_dsn(cls, dbname: str = None, db_name: str = None) -> dict:
        target_db = dbname or db_name or cls.NAME
        dsn = {
            "host": cls.HOST,
            "port": cls.PORT,
            "dbname": target_db,
            "user": cls.USER,
            "password": cls.PASSWORD,
        }
        if cls.SSLMODE:
            dsn["sslmode"] = cls.SSLMODE
        return dsn
