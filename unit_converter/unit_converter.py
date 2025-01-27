import reflex as rx
from typing import List, Dict


class State(rx.State):
    units: Dict[str, List[str]] = {
        "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    }
    convertions: Dict[str, Dict[str, float]] = {
        "Length": {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254,
        },
        "Weight": {
            "Grams": 0.001,
            "Kilograms": 1,
            "Pounds": 0.453592,
            "Ounces": 0.0283495,
        },
        "Temperature": {
            "Celsius": 1,
            "Fahrenheit": 0,
            "Kelvin": 0,
        },
    }
    categories: List[str] = ["Length", "Weight", "Temperature"]
    current_category: str = "Length"
    from_unit: str = ""
    to_unit: str = ""
    initial_value: float = 0
    final_value: float = 0
    show_results: bool = False

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
        self.show_results = False
        self.initial_value = 0
        self.final_value = 0

    @rx.event
    def handle_submit(self, form_data: dict) -> None:
        self.initial_value = float(form_data["value"])
        self.from_unit = form_data["from_unit"]
        self.to_unit = form_data["to_unit"]

        if self.current_category == "Temperature":
            self.convert_temperature()
            self.show_results = True
        else:
            self.convert()
            self.show_results = True

    @rx.event
    def change_screen(self) -> None:
        self.show_results = False
        self.final_value = 0
        self.initial_value = 0
        self.to_unit = ""
        self.from_unit = ""

    def convert(self) -> None:
        value_in_base = (
            self.initial_value * self.convertions[self.current_category][self.from_unit]
        )
        self.final_value = (
            value_in_base / self.convertions[self.current_category][self.to_unit]
        )

    def convert_temperature(self) -> None:
        if self.from_unit == "Celsius":
            if self.to_unit == "Fahrenheit":
                self.final_value = self.initial_value * 9 / 5 + 32
            elif self.to_unit == "Kelvin":
                self.final_value = self.initial_value + 273.15
            else:
                self.final_value = self.initial_value
        elif self.from_unit == "Fahrenheit":
            if self.to_unit == "Celsius":
                self.final_value = (self.initial_value - 32) * 5 / 9
            elif self.to_unit == "Kelvin":
                self.final_value = (self.initial_value - 32) * 5 / 9 + 273.15
            else:
                self.final_value = self.initial_value
        elif self.from_unit == "Kelvin":
            if self.to_unit == "Celsius":
                self.final_value = self.initial_value - 273.15
            elif self.to_unit == "Fahrenheit":
                self.final_value = (self.initial_value - 273.15) * 9 / 5 + 32
            else:
                self.final_value = self.initial_value


def create_trigger(category: str) -> rx.Component:
    return rx.tabs.trigger(category, value=category)


def create_content(category: str) -> rx.Component:
    return rx.tabs.content(
        rx.cond(
            State.show_results,
            rx.fragment(show_results()),
            rx.fragment(create_form(category)),
        ),
        value=category,
    )


def show_results() -> rx.Component:
    return rx.vstack(
        rx.text("Result of your calculation:"),
        rx.hstack(
            rx.text(State.initial_value),
            rx.text(State.from_unit),
            rx.text(" = "),
            rx.text(State.final_value),
            rx.text(State.to_unit),
        ),
        rx.button("Reset", on_click=State.change_screen),
    )


def create_form(category) -> rx.Component:
    return rx.form.root(
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
