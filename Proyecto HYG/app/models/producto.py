from sqlalchemy import Column, String, Text, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class Producto(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "hyg"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid()
    )

    tenant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("hyg.tenants.id"),
        nullable=False
    )

    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("hyg.categories.id"),
        nullable=True
    )

    unit_id = Column(
        UUID(as_uuid=True),
        ForeignKey("hyg.units.id"),
        nullable=True
    )

    code = Column(
        String,
        nullable=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    product_type = Column(
        String,
        nullable=False,
        server_default="INGREDIENT"
    )

    track_lots = Column(
        Boolean,
        nullable=False,
        server_default="false"
    )

    track_expiration = Column(
        Boolean,
        nullable=False,
        server_default="false"
    )

    minimum_stock = Column(
        Numeric,
        nullable=False,
        server_default="0"
    )

    maximum_stock = Column(
        Numeric,
        nullable=True
    )

    status = Column(
        String,
        nullable=False,
        server_default="ACTIVE"
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )