import os

from typing import TYPE_CHECKING

from src.controller.base import BaseController
from src.model.data_model import DataModel

if TYPE_CHECKING:
    from src.view.main_window import MainWindowView


class MainController(BaseController):
    view: 'MainWindowView'
    model: DataModel

    def __init__(self, view: 'MainWindowView') -> None:
        super().__init__(view, DataModel())

    def clear_view(self) -> None:
        self.view.clear()

    def draw(self) -> None:
        self.model.draw()
        self.view.render_image(self.model.image)

    def save_image(self) -> None:
        print("saving")
        self.model.image.save("./image.png")
