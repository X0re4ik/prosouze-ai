from src.entities.base_model import BaseModel
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    func,
)


class Promty(BaseModel):
    __tablename__ = "promty"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    text = Column(
        Text,
        nullable=False,
    )
    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
