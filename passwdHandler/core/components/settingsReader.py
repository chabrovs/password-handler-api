from base import SettingsReader
from ...management import SETTINGS
import json
from typing import Any


class PasswdSettings(SettingsReader):
    def __init__(self) -> None:
        super().__init__()
        self.settings_dict: dict = self.open_settings_file()

    def open_settings_file(setting) -> dict:
        with open(SETTINGS + 'settings.json', 'r') as file:
            data = json.load(file)
        
        return data
    
    def search_setting(self, setting: str) -> Any:
        """Return a specific value from a given key(setting) in a dictionary"""
        stack: list = []
        value: Any = None

        for key, value in self.settings_dict.items():
            if key == setting:
                value = setting
                break
            elif isinstance(value, dict):
                stack.append((key, value))

        while stack:
            key, value = stack.pop()
            if key in value:
                value = key[value]
                break
            elif isinstance(value, dict):
                stack.append((key, value))

        return value


    def read_setting(self, setting: str) -> dict[str: bool]:
        return self.settings_file[setting]

    def read_ascii_setting(self, setting: str ):
        pass