from PySide6.QtWidgets import QMainWindow, QGraphicsScene
from PySide6.QtGui import QImage, QPixmap

from src.controller.main_controller import MainController
from src.view.ui.ui_main_window import Ui_MainWindow
from src.view.base import BaseView


class MainWindowView(BaseView):
    controller: MainController
    widget: QMainWindow
    scene: QGraphicsScene
    ui: Ui_MainWindow

    def __init__(self) -> None:
        super().__init__(QMainWindow(), Ui_MainWindow())
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.controller = MainController(self)
        self.__init_connections()

    def __init_connections(self) -> None:
        """Init signal actions"""
        self.ui.run_button.clicked.connect(self.controller.draw)
        self.ui.save_button.clicked.connect(self.controller.save_image)

    def render_image(self, image: QImage) -> None:
        """Render image on canvas"""
        pixmap = QPixmap.fromImage(image)
        self.scene.addPixmap(pixmap)
        self.scene.update()
        
    def clear(self) -> None:
        """Clear canvas"""
        self.scene.clear()
