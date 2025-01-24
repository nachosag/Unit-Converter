import reflex as rx
from unit_converter.states.FormState import FormState
from .screens import results_screen, form_screen

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
                            results_screen(),
                            form_screen(),
                        ),
                        value="lenght_tab"
                    ),
                    rx.tabs.content(
                        rx.cond(
                            FormState.show_results,
                            results_screen(),
                            form_screen(),
                        ),
                        value="weight_tab"
                    ),
                    rx.tabs.content(
                        rx.cond(
                            FormState.show_results,
                            results_screen(),
                            form_screen(),
                        ),
                        value="temperature_tab"
                    )
                )
            )