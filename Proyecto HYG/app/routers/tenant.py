from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.tenant import Tenant
from app.schemas.tenant import (
    TenantCrear,
    TenantActualizar,
    TenantRespuesta,
)


router = APIRouter(
    prefix="/tenants",
    tags=["Organizaciones"]
)


# ============================================================
# DEPENDENCIA DE BASE DE DATOS
# ============================================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ============================================================
# LISTAR ORGANIZACIONES
# ============================================================

@router.get("/", response_model=List[TenantRespuesta])
def listar_tenants(
    db: Session = Depends(get_db)
):
    tenants = (
        db.query(Tenant)
        .order_by(Tenant.name)
        .all()
    )

    return tenants


# ============================================================
# CONSULTAR ORGANIZACIÓN POR ID
# ============================================================

@router.get("/{tenant_id}", response_model=TenantRespuesta)
def obtener_tenant(
    tenant_id: UUID,
    db: Session = Depends(get_db)
):
    tenant = (
        db.query(Tenant)
        .filter(Tenant.id == tenant_id)
        .first()
    )

    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Organización no encontrada"
        )

    return tenant


# ============================================================
# CREAR ORGANIZACIÓN
# ============================================================

@router.post(
    "/",
    response_model=TenantRespuesta,
    status_code=201
)
def crear_tenant(
    datos: TenantCrear,
    db: Session = Depends(get_db)
):
    tenant = Tenant(
        name=datos.name,
        business_type=datos.business_type,
        tax_id=datos.tax_id,
        phone=datos.phone,
        email=datos.email,
        address=datos.address,
        city=datos.city,
        country=datos.country,
        logo_url=datos.logo_url,
        status=datos.status,
    )

    db.add(tenant)
    db.commit()
    db.refresh(tenant)

    return tenant


# ============================================================
# ACTUALIZAR ORGANIZACIÓN
# ============================================================

@router.put(
    "/{tenant_id}",
    response_model=TenantRespuesta
)
def actualizar_tenant(
    tenant_id: UUID,
    datos: TenantActualizar,
    db: Session = Depends(get_db)
):
    tenant = (
        db.query(Tenant)
        .filter(Tenant.id == tenant_id)
        .first()
    )

    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Organización no encontrada"
        )

    cambios = datos.model_dump(
        exclude_unset=True
    )

    for campo, valor in cambios.items():
        setattr(tenant, campo, valor)

    db.commit()
    db.refresh(tenant)

    return tenant