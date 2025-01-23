import reflex as rx
from unit_converter.states.FormState import FormState
from unit_converter.states.SelectState import SelectState
from unit_converter.constants.Units import Units

def results_screen():
    return rx.vstack(
                    rx.heading("Results"),
                    rx.hstack(
                        rx.text(FormState.result.to_string()),
                    ),
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
                            rx.input(name="value", required=True),
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
                    )
                )