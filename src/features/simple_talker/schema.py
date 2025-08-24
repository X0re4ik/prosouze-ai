from pydantic import BaseModel


class RequestSchema(BaseModel):
    message: str


class ResponseSchema(BaseModel):
    answers: list[str]
