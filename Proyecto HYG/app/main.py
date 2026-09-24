from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routers import producto, tenant
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)


# ==========================================
# ROUTERS
# ==========================================

app.include_router(tenant.router)


# ==========================================
# INICIO
# ==========================================

@app.get("/", tags=["Sistema"])
def inicio():
    return {
        "mensaje": "HYG GASTRO-SOFT API funcionando correctamente",
        "version": settings.APP_VERSION,
    }


# ==========================================
# SALUD DE LA API Y BASE DE DATOS
# ==========================================

@app.get("/salud", tags=["Sistema"])
def salud():
    try:
        with engine.connect() as connection:
            resultado = connection.execute(text("SELECT 1"))
            resultado.scalar()

        return {
            "estado": "OK",
            "base_de_datos": "PostgreSQL conectada",
        }

    except Exception as e:
        return {
            "estado": "ERROR",
            "detalle": str(e),
        }