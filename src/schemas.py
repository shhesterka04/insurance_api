from pydantic import BaseModel, field_validator
import re


class Courier(BaseModel):
    rate: str
    cargo_type: str
    date: str

    @field_validator("cargo_type")
    def check_date_format(cls, date: str) -> str:
        pattern = r'\b(19|20)\d\d-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])\b'
        if not re.match(pattern, date):
            raise ValueError("Invalid date format. Expected format: 'YYYY-MM-DD'")
        return date


