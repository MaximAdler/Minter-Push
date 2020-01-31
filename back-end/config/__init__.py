import os
from config.app_config import config_by_name

APP_CONFIG = config_by_name.get(os.getenv('APP_ENV', 'DEV'))

__all__ = [
    'APP_CONFIG',
]