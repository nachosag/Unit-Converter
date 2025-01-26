import reflex as rx
from typing import List, Dict


class Category(rx.State):
    units: Dict[str, List[str]] = {
        "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    }
    categories: List[str] = ["Length", "Weight", "Temperature"]
    # available_units: list[str] = units["Length"]
    current_category: str = "Length"
    from_unit: str = " "
    to_unit: str = " "

    @rx.var
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
        self.from_unit = " "
        self.to_unit = " "
        # self.available_units = self.units[self.current_category]


def create_trigger(category: str) -> rx.Component:
    return rx.tabs.trigger(category, value=category)


def create_content(category: str) -> rx.Component:
    return rx.tabs.content(
        rx.vstack(
            rx.select.root(
                rx.select.trigger(placeholder="From unit"),
                rx.select.content(
                    rx.select.group(
                        rx.foreach(
                            Category.get_available_units,
                            lambda x: rx.select.item(x, value=x),
                        )
                    )
                ),
                value=Category.from_unit,
                on_change=Category.set_from_unit,
            )
        ),
        value=category,
    )
    # ,
    # rx.select.root(
    #     rx.select.trigger(placeholder="To unit"),
    #     rx.select.content(
    #         rx.select.group(
    #             rx.foreach(
    #                 Category.available_units,
    #                 lambda x: rx.select.item(x, value=x),
    #             )
    #         )
    #     ),
    #     value=Category.to_unit,
    #     on_change=Category.set_to_unit,
    # ),


def tabs() -> rx.Component:
    return rx.hstack(
        rx.tabs.root(
            rx.tabs.list(rx.foreach(Category.categories, create_trigger)),
            rx.foreach(Category.categories, create_content),
            value=Category.current_category,
            on_change=Category.change_category,
        )
    )
