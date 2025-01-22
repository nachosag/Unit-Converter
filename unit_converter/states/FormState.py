import reflex as rx

class FormState(rx.State):
    show_results: bool = False
    form_data: dict

    @rx.event
    def handle_submit(self, form_data: dict):
        # Logica de conversion
        self.form_data = form_data
        self.show_results = True
    
    @rx.event
    def reset_screen(self):
        self.form_data = {}
        self.show_results = False