from typing import TYPE_CHECKING

from PySide6.QtGui import QResizeEvent

from src.controller.base import BaseController
from src.utils.render import Renderer

if TYPE_CHECKING:
    from src.model.data_model import DataModel
    from src.view.main_window import MainWindowView


class MainController(BaseController):
    view: 'MainWindowView'
    model: 'DataModel'

    def __init__(self, model: 'DataModel', view: 'MainWindowView') -> None:
        super().__init__(model, view)
        self.__init_connections()

    def __init_connections(self) -> None:
        """Init signal actions"""
        self.view.ui.run_button.clicked.connect(self.handle_run_button_click)
        self.view.ui.save_button.clicked.connect(self.handle_save_button_click)

        self.view.ui.graphicsView.resizeEvent = self.__resize_canvas_event  # type: ignore

    def __resize_canvas_event(self, event: QResizeEvent) -> None:
        self.update_canvas()

    def update_canvas(self) -> None:
        renderer = Renderer([])
        image = renderer.render(self.view.ui.graphicsView.width(), self.view.ui.graphicsView.height())
        self.view.upload_image(image)

    def clear_view(self) -> None:
        self.view.clear()

    def handle_run_button_click(self) -> None:
        self.update_canvas()

    def handle_save_button_click(self) -> None:
        self.model.image.save("./image.png")
