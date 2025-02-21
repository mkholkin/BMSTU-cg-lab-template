from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.view.base import BaseView
    from src.model.data_model import DataModel


class BaseController(ABC):
    model: 'DataModel'
    view: 'BaseView'

    def __init__(self, model: 'DataModel', view: 'BaseView'):
        self.model = model
        self.view = view
