import reflex as rx
from unit_converter.states.FormState import FormState
from unit_converter.states.SelectState import SelectState
from unit_converter.constants.Units import Units

def results_screen():
    return rx.vstack(
        rx.heading("Results"),
        rx.hstack(
            rx.text(FormState.result["result"]),
            rx.text(FormState.result["convert_to"])
        ),
        rx.button(
            "Reset",
            on_click=FormState.reset_screen
        )
    )
    
def form_screen():
    return rx.vstack(
        rx.form.root(
            rx.form.field(
                rx.form.label("Enter the lenght to convert"),
                rx.form.control(
                    rx.input(
                        name="value",
                        required=True,
                        type="number"
                    ),
                    as_child=True
                ),
                rx.form.message(
                    "Please enter a valid number",
                    match="typeMismatch"
                ),
                name="lenght_field"
            ),
            rx.form.field(
                rx.form.label("Unit to convert from"),
                rx.select(
                    Units.LENGHT.value,
                    name="convert_from",
                    placeholder="Select an option",
                    on_change=SelectState.convert_from,
                    required=True,
                ),
                name="from_unit_field"
            ),
            rx.form.field(
                rx.form.label("Unit to convert to"),
                rx.select(
                    Units.LENGHT.value,
                    name="convert_to",
                    placeholder="Select an option",
                    on_change=SelectState.convert_to,
                    required=True
                ),
                name="to_unit_field"
            ),
            rx.button(
                "Convert",
                type="submit"
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=False
        )
    )