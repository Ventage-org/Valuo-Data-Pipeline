"""
Configuración centralizada del Pipeline de Datos (ETL).
Recolección, limpieza y almacenamiento en PostgreSQL para valoración inmobiliaria.
"""
from pathlib import Path

# Directorio raíz del proyecto (un nivel arriba de src/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Rutas de datos
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Archivos fuente primarios del BCRP
DATASET_FILENAME = "dataset_entrenamiento_venta_2025.xlsx"
DATASET_PATH = DATA_RAW_DIR / DATASET_FILENAME

DATASET_ALQUILER_FILENAME = "dataset_entrenamineto_alquiler_2025.xlsx"
DATASET_ALQUILER_PATH = DATA_RAW_DIR / DATASET_ALQUILER_FILENAME

# Tabla maestra de contexto distrital-anual (Single Source of Truth)
DISTRICT_CONTEXT_PATH = DATA_PROCESSED_DIR / "distrito_anio_contexto.csv"

# Targets y variables clave
TARGET_COL = "Precio_Soles_Const"
TARGET_ALQUILER_COL = "Alquiler_Soles_Const"
COL_DISTRITO = "Distrito"

# Partición temporal
TRAIN_YEARS = list(range(2016, 2024))  # 2016–2023
TEST_YEARS = list(range(2024, 2026))   # 2024–2025
SPLIT_COL = "Anio"
