import reflex as rx
from unit_converter.constants.Units import Units

class FormState(rx.State):
    show_results: bool = False
    initial_value: float = 0.0
    convert_from: str = ""
    final_value: float = 0.0
    convert_to: str = ""

    @rx.event
    def handle_submit(self, form_data: dict):
        try:
            self.initial_value = float(form_data["value"])
            self.convert_from = form_data["convert_from"]
            self.convert_to = form_data["convert_to"]
            self.convert()
            self.show_results = True
            
        except Exception as e:
            raise "Hubo un error en la inicializacion de datos"
    
    @rx.event
    def reset_screen(self):
        self.show_results = False

    def convert(self):
        try:
            self.final_value = self.initial_value * Units.LENGHT_UNITS.value[f"{self.convert_from}"]
            self.final_value = self.final_value / Units.LENGHT_UNITS.value[f"{self.convert_to}"]
        except Exception as e:
            raise "Hubo un error en la conversión de datos"