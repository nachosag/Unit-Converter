import reflex as rx
from unit_converter.components.Select import *

def convert_form(options: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text("Unit to convert from"),
            rx.select(
                options,
                value=Select.from_unit,
                on_change=Select.convert_from()
            ),
            rx.text("Unit to convert to"),
            rx.select(
                options,
                value=Select.to_unit,
                on_change=Select.convert_to()
            )
    )