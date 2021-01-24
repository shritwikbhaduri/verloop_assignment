
from pydantic import BaseModel, Field, validator
from settings import get_settings

settings = get_settings()


class AddressDetailRequest(BaseModel):
    address: str = Field(..., description="requested address in human readable form")
    output_format: str = Field(..., description="returned data formal, json or xml")

    @validator("output_format")
    def validate_output_format(cls, flag: str):
        if flag.upper() not in settings.SUPPORTED_OUTPUT_FORMAT:
            raise ValueError(f"requested output format cannot be processed. allowed output format are {settings.SUPPORTED_OUTPUT_FORMAT}")
        else:
            return flag
