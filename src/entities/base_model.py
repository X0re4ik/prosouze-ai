from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {
        "schema": "ai_prosouze",
    }
