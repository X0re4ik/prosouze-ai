from fastapi import APIRouter

from .v1 import v1_route

app_route = APIRouter(prefix="/ai-prosouze")

app_route.include_router(
    v1_route,
)
