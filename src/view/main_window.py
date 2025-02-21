from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QFrame

from src.view.base import BaseView
from src.view.ui.ui_main_window import Ui_MainWindow


class MainWindowView(BaseView):
    widget: QMainWindow
    scene: QGraphicsScene
    ui: Ui_MainWindow

    def __init__(self) -> None:
        super().__init__(QMainWindow(), Ui_MainWindow())
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setFrameShape(QFrame.NoFrame)
        self.ui.graphicsView.setScene(self.scene)

    def upload_image(self, image: QImage) -> None:
        """Upload image on canvas"""
        self.scene.clear()
        pixmap = QPixmap.fromImage(image)
        pixmap_item = self.scene.addPixmap(pixmap)
        self.scene.setSceneRect(pixmap_item.boundingRect())

    def clear(self) -> None:
        """Clear canvas"""
        self.scene.clear()
