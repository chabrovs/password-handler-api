from abc import ABC, abstractmethod


class CSVManager(ABC):
    @abstractmethod
    def check_existence() -> bool:
        """Checks if CSV file exist in the directory set in the settings."""
        ...
    
    @abstractmethod
    def save_record() -> None:
        """Save record to the csv file."""
        ...


class CSVRecordSaver(CSVManager):
    def save_record(self, password: str) -> None:
        """Saves record to CSV file"""
        ...