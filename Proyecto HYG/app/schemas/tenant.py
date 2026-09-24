from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class TenantBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=255
    )

    business_type: str = Field(
        default="OTHER",
        max_length=50
    )

    tax_id: Optional[str] = Field(
        default=None,
        max_length=100
    )

    phone: Optional[str] = Field(
        default=None,
        max_length=50
    )

    email: Optional[str] = Field(
        default=None,
        max_length=255
    )

    address: Optional[str] = Field(
        default=None,
        max_length=255
    )

    city: Optional[str] = Field(
        default=None,
        max_length=100
    )

    country: str = Field(
        default="Colombia",
        max_length=100
    )

    logo_url: Optional[str] = None

    status: str = Field(
        default="ACTIVE",
        max_length=50
    )


class TenantCrear(TenantBase):
    pass


class TenantActualizar(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    business_type: Optional[str] = Field(
        default=None,
        max_length=50
    )

    tax_id: Optional[str] = Field(
        default=None,
        max_length=100
    )

    phone: Optional[str] = Field(
        default=None,
        max_length=50
    )

    email: Optional[str] = Field(
        default=None,
        max_length=255
    )

    address: Optional[str] = Field(
        default=None,
        max_length=255
    )

    city: Optional[str] = Field(
        default=None,
        max_length=100
    )

    country: Optional[str] = Field(
        default=None,
        max_length=100
    )

    logo_url: Optional[str] = None

    status: Optional[str] = Field(
        default=None,
        max_length=50
    )


class TenantRespuesta(TenantBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)