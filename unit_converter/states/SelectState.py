import reflex as rx

class SelectState(rx.State):
    from_unit: str = "  "
    to_unit: str = "  "

    @rx.event
    def convert_from(self, value: str):
        self.from_unit = value
        
    @rx.event
    def convert_to(self, value: str):
        self.to_unit = value