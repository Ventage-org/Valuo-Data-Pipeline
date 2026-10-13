# =============================================================================
# DOCKERFILE - PIPELINE DE INGESTA INMOBILIARIA (ETL)
# Optimizado para Azure Container Apps Jobs / Azure Container Instances
# =============================================================================

FROM python:3.10-slim

# Evitar generación de .pyc y forzar logging en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Instalar dependencias del sistema para PostgreSQL y compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente, scripts SQL y datasets necesarios
COPY src/ /app/src/
COPY sql/ /app/sql/
COPY data/ /app/data/

# Usuario seguro no-root
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Comando por defecto: ejecutar pipeline de ingesta completo
ENTRYPOINT ["python", "-m", "src.etl.run_etl"]
CMD ["--run-all"]
