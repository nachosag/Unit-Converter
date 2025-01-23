from enum import Enum

class Units(Enum):
    LENGHT: list[str] = [
        "Select an option",
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
        "Select an option",
        "Milligram", 
        "Gram", 
        "Kilogram", 
        "Ounce", 
        "Pound"
    ]
    
    TEMPERATURE: list[str] = [
        "Select an option",
        "Celsius", 
        "Fahrenheit", 
        "Kelvin"
    ]
    
    LENGHT_UNITS = {
        "Meter": 1,  # Unidad base para longitud
        "Centimeter": 0.01,  # 1 cm = 0.01 m
        "Kilometer": 1000,  # 1 km = 1000 m
        "Millimeter": 0.001,  # 1 mm = 0.001 m
        "Inch": 0.0254,  # 1 inch = 0.0254 m
        "Foot": 0.3048,  # 1 foot = 0.3048 m
        "Yard": 0.9144,  # 1 yard = 0.9144 m
        "Mile": 1609.34,  # 1 mile = 1609.34 m
    }