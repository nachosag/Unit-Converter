from enum import Enum

class Units(Enum):
    LENGHT: list[str] = [
        "Millimeter", 
        "Centimeter", 
        "Meter", 
        "Kilometer", 
        "Inch", 
        "Foot", 
        "Yard", 
        "Mile"
    ]
    
    WEIGHT: list[str] = [
        "Milligram", 
        "Gram", 
        "Kilogram", 
        "Ounce", 
        "Pound"
    ]
    
    TEMPERATURE: list[str] = [
        "Celsius", 
        "Fahrenheit", 
        "Kelvin"
    ]