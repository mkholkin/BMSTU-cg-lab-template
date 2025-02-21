import sys

from PySide6.QtWidgets import QApplication

from src.controller.main_controller import MainController
from src.model.data_model import DataModel
from src.view.main_window import MainWindowView


def main() -> None:
    app = QApplication(sys.argv)

    model = DataModel()
    view = MainWindowView()
    MainController(model, view)

    window = view.widget
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
