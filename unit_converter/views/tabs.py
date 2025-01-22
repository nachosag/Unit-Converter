import reflex as rx
from unit_converter.constants.units import Units
from unit_converter.views.convert_form import convert_form

def tabs() -> rx.Component:
    return rx.hstack(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger("Lenght", value="lenght_tab"),
                        rx.tabs.trigger("Weight", value="weight_tab"),
                        rx.tabs.trigger("Temperature", value="temperature_tab")
                    ),
                    rx.tabs.content(
                        rx.text("Enter the lenght to convert"),
                        rx.input(),
                        convert_form(Units.LENGHT.value),
                        value="lenght_tab"
                    ),
                    # rx.tabs.content(
                    #     rx.text("Enter the weight to convert"),
                    #     rx.input(),
                        
                    #     value="weight_tab"
                    # ),
                    # rx.tabs.content(
                    #     rx.text("Enter the temperature to convert"),
                    #     rx.input(),
                        
                    #     value="temperature_tab"
                    # )
                )
            )