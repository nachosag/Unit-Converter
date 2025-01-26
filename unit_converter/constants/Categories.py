from enum import Enum


class Categories(Enum):
    LENGTH: str = "LENGTH"
    WEIGHT: str = "WEIGHT"
    TEMPERATURE: str = "TEMPERATURE"

    CATEGORIES: list[str] = ["Length", "Weight", "Temperature"]
