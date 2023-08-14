import json
from typing import Any
from pathlib import Path
import os
from abc import ABC, abstractmethod

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SETTINGS = os.path.join(BASE_DIR, "settings.json", )


class SettingsReader(ABC):
    def __init__(self) -> None: ...

    @abstractmethod
    def load_settings() -> dict:
        """Opens settings file and extracts data from it"""
        ...

    @abstractmethod
    def read_all() -> dict[str: Any]:
        """Returns all settings form settings.json"""
        ...

    @abstractmethod
    def read_setting() -> Any:
        """Returns specific setting form settings.json"""
        ...


class Manager(SettingsReader):
    def __init__(self) -> None:
        super().__init__()
        self.settings_data: dict = self.load_settings()

    def load_settings(self) -> dict:
        with open(SETTINGS, 'r') as file:
            settings_data = json.load(file)

        return settings_data

    def read_setting(self, setting: str) -> Any:
        raise NotImplementedError

    def read_all(self) -> dict:
        raise NotImplementedError

    def read_ascii_setting(self, setting: str):
        raise NotImplementedError
