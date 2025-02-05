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
