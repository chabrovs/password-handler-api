from abc import ABC, abstractmethod
from pathlib import Path
import os
# from .procedures import 

class Execute(ABC):
    @abstractmethod
    def Execute():
        """Execute commands to work with the program"""
        ...

BASE_DIR = Path(__file__).resolve().parent
SETTINGS = os.path.join(BASE_DIR, "core", )

def execute_from_command_line(self, arguments: list[str]):
    raise NotImplementedError