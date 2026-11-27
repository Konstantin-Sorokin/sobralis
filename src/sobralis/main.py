import uvicorn
from sobralis.core.config import settings
from sobralis.core.logging import configure_logging
from sobralis.create_app import create_app

configure_logging()

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "sobralis.main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
