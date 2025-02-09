from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.view.base import BaseView
    from src.model.data_model import DataModel


class BaseController(ABC):
    view: 'BaseView'
    model: 'DataModel'

    def __init__(self, view: 'BaseView', model: 'DataModel'):
        self.view = view
        self.model = model
