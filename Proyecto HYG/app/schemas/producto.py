from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductoBase(BaseModel):
    tenant_id: UUID
    category_id: Optional[UUID] = None
    unit_id: Optional[UUID] = None

    code: Optional[str] = Field(
        default=None,
        max_length=100
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=255
    )

    description: Optional[str] = None

    product_type: str = Field(
        default="INGREDIENT",
        max_length=50
    )

    track_lots: bool = False

    track_expiration: bool = False

    minimum_stock: Decimal = Field(
        default=Decimal("0"),
        ge=0
    )

    maximum_stock: Optional[Decimal] = Field(
        default=None,
        ge=0
    )

    status: str = Field(
        default="ACTIVE",
        max_length=50
    )


class ProductoCrear(ProductoBase):
    pass


class ProductoActualizar(BaseModel):
    category_id: Optional[UUID] = None
    unit_id: Optional[UUID] = None

    code: Optional[str] = Field(
        default=None,
        max_length=100
    )

    name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    description: Optional[str] = None

    product_type: Optional[str] = Field(
        default=None,
        max_length=50
    )

    track_lots: Optional[bool] = None

    track_expiration: Optional[bool] = None

    minimum_stock: Optional[Decimal] = Field(
        default=None,
        ge=0
    )

    maximum_stock: Optional[Decimal] = Field(
        default=None,
        ge=0
    )

    status: Optional[str] = Field(
        default=None,
        max_length=50
    )


class ProductoRespuesta(ProductoBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )