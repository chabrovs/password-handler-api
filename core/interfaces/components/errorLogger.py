from abc import ABC, abstractmethod


class ErrorLogger(ABC):
    @abstractmethod
    def LogError() -> None:
        """Logs error"""
        ...


class FileErrorLogger(ErrorLogger):
    def __init__(self) -> None:
        super().__init__()
        self.keyExistenceErrorMessageTemplate = "Key error: Key already exist!"
        self.keyNotFoundErrorMessageTemplate = "Key error: Key not found!"
    
    def LogError(self) -> None:
        """Logs Error if keys do not exist on the server"""
        ...
    
    def LogErrorKeyAlreadyExist(self) -> None:
        """Logs Error if keys do not exist on the server"""
        with open("ErrorLogs.txt", 'a') as error_logs_file:
            error_logs_file.write(self.keyExistenceErrorMessageTemplate + "\n")

    def LogErrorKeyNotFound(self) ->  None:
        """Logs Error if key was not found"""
        with open("ErrorLogs.txt", 'a') as error_logs_file:
            error_logs_file.write(self.keyNotFoundErrorMessageTemplate + "\n")