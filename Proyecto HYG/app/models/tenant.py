from sqlalchemy import Column, String, Text, DateTime, text
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Tenant(Base):
    __tablename__ = "tenants"
    __table_args__ = {
        "schema": "hyg"
    }

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    name = Column(
        String,
        nullable=False
    )

    business_type = Column(
        String,
        nullable=False,
        server_default=text("'OTHER'")
    )

    tax_id = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    email = Column(
        String,
        nullable=True
    )

    address = Column(
        String,
        nullable=True
    )

    city = Column(
        String,
        nullable=True
    )

    country = Column(
        String,
        nullable=False,
        server_default=text("'Colombia'")
    )

    logo_url = Column(
        Text,
        nullable=True
    )

    status = Column(
        String,
        nullable=False,
        server_default=text("'ACTIVE'")
    )

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()")
    )