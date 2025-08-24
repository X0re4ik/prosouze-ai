from pydantic import BaseModel, Field

from typing import TypeVar, Generic


T = TypeVar("T")


class ResponseBaseModel(BaseModel, Generic[T]):
    data: T
    error: str | None = Field(
        default=None,
    )
