from abc import ABC, abstractmethod


class Execute(ABC):
    @abstractmethod
    def Execute():
        """Execute commands to work with the program"""
        ...


print(BASE_DIR)
def execute_from_command_line(self, arguments: list[str]):
    raise NotImplementedError