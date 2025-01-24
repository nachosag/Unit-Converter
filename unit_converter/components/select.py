import reflex as rx

def select(label: str, options: list, on_change: callable, select_name: str, form_name: str) -> rx.Component:
    return rx.vstack(
        rx.form.label(label),
        rx.select(
            options,
            name=select_name,
            placeholder="Select an option",
            on_change=on_change,
            required=True
        ),
        name=form_name
    )