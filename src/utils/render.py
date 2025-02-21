from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Optional

from PySide6.QtGui import QPainter, QColor, QImage


@dataclass
class Style:
    border_color: QColor
    fill_color: QColor

    def __init__(self, border_color: QColor = QColor("black"), fill_color: QColor = QColor(None)) -> None:
        self.border_color = border_color
        self.fill_color = fill_color


@dataclass
class Scale:
    x: float
    y: float

    def __init__(self, x: float = 1, y: float = 1) -> None:
        self.x = x
        self.y = y


@dataclass
class Offset:
    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y


@dataclass
class Rotation:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Renderer:
    drawables: list['Drawable']

    def __init__(self, drawables: list['Drawable']):
        self.drawables = drawables

    def render(self, width: int, height: int, drawables: Iterable['Drawable'] = None) -> QImage:
        if drawables is None:
            drawables = self.drawables

        image = QImage(width, height, QImage.Format.Format_RGB32)
        painter = QPainter(image)

        for drawable in drawables:
            drawable.transform().draw(painter)

        painter.end()
        return image


class Drawable(ABC):
    style: Style

    scale: Scale
    offset: Offset
    rotation: Rotation

    @abstractmethod
    def occupied_rect(self) -> tuple[float, float, float, float]:
        pass

    @abstractmethod
    def draw(self, painter: QPainter, style: Optional[Style] = None) -> None:
        pass

    @abstractmethod
    def transform(self,
                  rotation: Optional[Rotation] = None,
                  offset: Optional[Offset] = None,
                  scale: Optional[Scale] = None,
                  origin_offset: Optional[Offset] = None) -> 'Drawable':
        pass


class ComponentDrawable(Drawable):
    @abstractmethod
    def occupied_rect(self) -> tuple[float, float, float, float]:
        pass

    @abstractmethod
    def draw(self, painter: QPainter, style: Optional[Style] = None) -> None:
        pass

    @abstractmethod
    def transform(self,
                  rotation: Optional[Rotation] = None,
                  offset: Optional[Offset] = None,
                  scale: Optional[Scale] = None,
                  origin_offset: Optional[Offset] = None) -> 'ComponentDrawable':
        pass


class CompositeDrawable(Drawable):
    items: list[Drawable]

    @abstractmethod
    def occupied_rect(self) -> tuple[float, float, float, float]:
        pass

    @abstractmethod
    def draw(self, painter: QPainter, style: Optional[Style] = None) -> None:
        pass

    @abstractmethod
    def transform(self,
                  rotation: Optional[Rotation] = None,
                  offset: Optional[Offset] = None,
                  scale: Optional[Scale] = None,
                  origin_offset: Optional[Offset] = None) -> 'CompositeDrawable':
        pass
