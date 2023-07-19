from abc import ABC, abstractmethod
from typing import Any
# https://www.athome.lu/location/appartement/luxembourg/id-7952705.html
class SettingsReader(ABC):
    def __init__(self) -> None: ...

    @abstractmethod
    def open_settings_file() -> dict:
        """Opens settings file and extracts data from it"""
    
    @abstractmethod
    def read_all():
        """Returns all settings form settings.json"""

    @abstractmethod
    def read_setting():
        """Returns specific setting form settings.json"""

   