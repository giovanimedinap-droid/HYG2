from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.producto import Producto
from app.schemas.producto import (
    ProductoCrear,
    ProductoActualizar,
    ProductoRespuesta,
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


# ==========================================
# DEPENDENCIA DE BASE DE DATOS
# ==========================================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ==========================================
# LISTAR PRODUCTOS
# ==========================================

@router.get("/", response_model=List[ProductoRespuesta])
def listar_productos(
    db: Session = Depends(get_db)
):
    productos = (
        db.query(Producto)
        .order_by(Producto.name)
        .all()
    )

    return productos


# ==========================================
# OBTENER PRODUCTO POR ID
# ==========================================

@router.get(
    "/{producto_id}",
    response_model=ProductoRespuesta
)
def obtener_producto(
    producto_id: UUID,
    db: Session = Depends(get_db)
):
    producto = (
        db.query(Producto)
        .filter(Producto.id == producto_id)
        .first()
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


# ==========================================
# CREAR PRODUCTO
# ==========================================

@router.post(
    "/",
    response_model=ProductoRespuesta,
    status_code=201
)
def crear_producto(
    producto: ProductoCrear,
    db: Session = Depends(get_db)
):
    nuevo_producto = Producto(
        **producto.model_dump()
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


# ==========================================
# ACTUALIZAR PRODUCTO
# ==========================================

@router.put(
    "/{producto_id}",
    response_model=ProductoRespuesta
)
def actualizar_producto(
    producto_id: UUID,
    producto_data: ProductoActualizar,
    db: Session = Depends(get_db)
):
    producto = (
        db.query(Producto)
        .filter(Producto.id == producto_id)
        .first()
    )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    datos = producto_data.model_dump(
        exclude_unset=True
    )

    for campo, valor in datos.items():
        setattr(producto, campo, valor)

    db.commit()
    db.refresh(producto)

    return producto