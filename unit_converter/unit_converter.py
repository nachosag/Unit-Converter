import reflex as rx
from unit_converter.constants.Units import Units
from unit_converter.states.SelectState import SelectState
from unit_converter.states.FormState import FormState

def index() -> rx.Component:
    return rx.container(
            rx.vstack(
            rx.heading("Unit Converter"),
            tabs(),
            align="center"
        )
    )

def tabs():
    return rx.hstack(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger("Lenght", value="lenght_tab"),
                        rx.tabs.trigger("Weight", value="weight_tab"),
                        rx.tabs.trigger("Temperature", value="temperature_tab")
                    ),
                    rx.tabs.content(
                        rx.cond(
                            FormState.show_results,
                            # Results screen
                            results_screen(),
                            # Form screen 
                            form_screen(),
                        ),
                        value="lenght_tab"
                    )
                )
            )

def results_screen():
    return rx.vstack(
                    rx.heading("Results"),
                    rx.text(FormState.form_data.to_string()),
                    rx.button(
                        "Reset",
                        on_click=FormState.reset_screen,
                    ),
                )

def form_screen():
    return rx.vstack(
                    rx.text("Enter the lenght to convert"),
                    rx.form(
                        rx.vstack(
                            rx.input(name="input"),
                            rx.text("Unit to convert from"),
                            rx.select(
                            Units.LENGHT.value,
                            value=SelectState.from_unit,
                            on_change=SelectState.convert_from,
                            name="convert_from"
                            ),
                            rx.text("Unit to convert to"),
                            rx.select(
                                Units.LENGHT.value,
                                value=SelectState.to_unit,
                                on_change=SelectState.convert_to,
                                name="convert_to"
                            ),
                            rx.button(
                                "Submit",
                                type="submit"
                            )
                        ),
                        on_submit=FormState.handle_submit,
                        reset_on_submit=True
                    ),
                )

app = rx.App()
app.add_page(index)