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

import os

# Partición temporal configurable por trimestre
# Todo registro con (anio * 4 + trimestre) <= (CORTE_TRAIN_ANIO * 4 + CORTE_TRAIN_TRIMESTRE) será 'TRAIN'
# Por defecto: 2023-Q4 (hasta 2023-4 es TRAIN; 2024 en adelante es TEST) para alineación estricta con la tesis
CORTE_TRAIN_ANIO = int(os.getenv("CORTE_TRAIN_ANIO", "2023"))
CORTE_TRAIN_TRIMESTRE = int(os.getenv("CORTE_TRAIN_TRIMESTRE", "4"))
SPLIT_COL = "Anio"
