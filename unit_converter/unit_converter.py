import reflex as rx
from unit_converter.views.tabs import tabs

def index() -> rx.Component:
    return rx.container(
            rx.vstack(
            rx.heading("Unit Converter"),
            tabs(),
            align="center"
        )
    )


app = rx.App()
app.add_page(index)
