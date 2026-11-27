from fastapi import APIRouter
from sobralis.core.config import settings

router = APIRouter(prefix=settings.api.prefix)
