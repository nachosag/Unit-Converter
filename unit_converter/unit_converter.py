import reflex as rx
from typing import List, Dict


class State(rx.State):
    units: Dict[str, List[str]] = {
        "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    }
    data: Dict[str, str] = {"value": "", "from_unit": "", "to_unit": ""}
    categories: List[str] = ["Length", "Weight", "Temperature"]
    current_category: str = "Length"
    from_unit: str = ""
    to_unit: str = ""

    @rx.var(cache=True)
    def get_available_units(self) -> list[str]:
        return self.units[self.current_category]

    @rx.event
    def set_from_unit(self, value: str) -> None:
        self.from_unit = value

    @rx.event
    def set_to_unit(self, value: str) -> None:
        self.to_unit = value

    @rx.event
    def change_category(self, category: str) -> None:
        self.current_category = category
        self.from_unit = ""
        self.to_unit = ""

    @rx.event
    def handle_submit(self, form_data: dict) -> None:
        self.data = form_data
        print(self.data)


def create_trigger(category: str) -> rx.Component:
    return rx.tabs.trigger(category, value=category)


def create_content(category: str) -> rx.Component:
    return rx.tabs.content(
        rx.form.root(
            rx.form.field(
                rx.form.label(f"Enter the {category.lower()} to convert"),
                rx.form.control(
                    rx.input(
                        placeholder="Enter a value",
                        name="value",
                        type="number",
                        required=True,
                    ),
                    as_child=True,
                ),
                rx.form.message(
                    "Please enter a valid email",
                    match="typeMismatch",
                ),
            ),
            rx.vstack(
                rx.select.root(
                    rx.select.trigger(placeholder="Unit to convert from"),
                    rx.select.content(
                        rx.select.group(
                            rx.foreach(
                                State.get_available_units,
                                lambda x: rx.select.item(x, value=x),
                            )
                        )
                    ),
                    value=State.from_unit,
                    on_change=State.set_from_unit,
                    name="from_unit",
                    required=True,
                ),
                rx.select.root(
                    rx.select.trigger(placeholder="Unit to convert to"),
                    rx.select.content(
                        rx.select.group(
                            rx.foreach(
                                State.get_available_units,
                                lambda x: rx.select.item(x, value=x),
                            )
                        )
                    ),
                    value=State.to_unit,
                    on_change=State.set_to_unit,
                    name="to_unit",
                    required=True,
                ),
                rx.form.submit(
                    rx.button("Submit"),
                    as_child=True,
                ),
                required=True,
            ),
            on_submit=State.handle_submit,
            reset_on_submit=True,
        ),
        value=category,
    )


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Unit Converter"),
            rx.hstack(
                rx.tabs.root(
                    rx.tabs.list(rx.foreach(State.categories, create_trigger)),
                    rx.foreach(State.categories, create_content),
                    value=State.current_category,
                    on_change=State.change_category,
                )
            ),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
