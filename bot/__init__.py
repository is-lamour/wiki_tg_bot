from . import config
from . import loader
from . import main
from . import loader  # Сначала загружаем bot
from .handlers import default_handlers, custom_handlers  # Затем обработчики
