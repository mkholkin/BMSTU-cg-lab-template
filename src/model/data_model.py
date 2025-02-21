from PySide6.QtCore import QPoint
from PySide6.QtGui import QImage, QPainter, QPen, QBrush, QColor, QPolygon


class DataModel:
    image: QImage

    def __init__(self) -> None:
        self.image = QImage(1000, 1000, QImage.Format.Format_ARGB32)
        self.image.fill(QColor("transparent"))

    def draw(self) -> None:
        painter = QPainter(self.image)
        painter.setPen(QPen(QColor("green")))
        painter.setBrush(QBrush(QColor("red")))

        painter.drawPolygon(QPolygon([QPoint(0, 0), QPoint(100, 60), QPoint(60, 100)]))

        painter.end()
