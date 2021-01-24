from pydantic import SecretStr
import os

from pydantic.tools import lru_cache


class AppSettings:
    GEOCODE_API_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode"
    BASE_DIR: str = os.path.abspath(__file__)


class Production(AppSettings):
    SUPPORTED_OUTPUT_FORMAT = os.environ.get("OUTPUT_FORMAT", ["XML", "JSON", "BINARY"])
    GEO_CODE_API_KEY: SecretStr = os.environ.get('GEOCODE_API_KEY', "AIzaSyAQpU0XzCcn0QGf-71pqWZfC0rAc_Ueycw")


class Integration(AppSettings):
    SUPPORTED_OUTPUT_FORMAT = os.environ.get("OUTPUT_FORMAT", ["XML", "JSON"])
    GEO_CODE_API_KEY: SecretStr = os.environ.get('GEOCODE_API_KEY', "AIzaSyAQpU0XzCcn0QGf-71pqWZfC0rAc_Ueycw")


@lru_cache
def get_settings(env: str = os.environ.get('ENV', "integration")):
    if env.lower() == 'integration':
        return Integration()
    elif env.lower() == 'production':
        return Production()
    else:
        return Integration()
