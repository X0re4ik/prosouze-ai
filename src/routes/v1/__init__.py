from src.features.simple_talker import simple_talker_route

from fastapi import APIRouter

v1_route = APIRouter(
    prefix="/v1",
)


v1_route.include_router(
    simple_talker_route,
)
