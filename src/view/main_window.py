from PySide6.QtWidgets import QMainWindow
from src.controller.main_controller import MainController
from src.view.ui.ui_main_window import Ui_MainWindow
from src.view.base import BaseView


class MainWindowView(BaseView):
    controller: MainController
    widget: QMainWindow

    def __init__(self) -> None:
        super().__init__(QMainWindow(), Ui_MainWindow())
        self.controller = MainController(self)
