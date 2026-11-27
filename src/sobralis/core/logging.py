import logging

from sobralis.core.config import settings


def configure_logging() -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.logging.log_format,
    )
