import reflex as rx
from unit_converter.constants.Units import Units

class FormState(rx.State):
    show_results: bool = False
    result: float = 0

    @rx.event
    def handle_submit(self, form_data: dict):      
        
        self.verify(form_data["value"])
        self.convert(float(form_data["value"]), form_data["convert_from"], form_data["convert_to"])
            
        
        self.show_results = True
    
    @rx.event
    def reset_screen(self):
        self.show_results = False
        
    def convert(self, input: float, convert_from: str, convert_to: str):
        
        try:
            self.result = input * Units.LENGHT_UNITS.value[f"{convert_from}"]
            self.result = self.result / Units.LENGHT_UNITS.value[f"{convert_to}"]
        except Exception as e:
            self.results = -1
            
    def verify(self, value: str):
        pass