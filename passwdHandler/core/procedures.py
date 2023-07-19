from components.encryptor import Encryption, Decryption
from components.generator import (
    FilenameGenerator, 
    SuffixGenerator, 
    PasswordGenerator, 
    GenerateKeys
)
from components.keyManager import ReadPublicKeyFromFile, ReadPrivateKeyFile
from components.errorLogger import FileErrorLogger
from abc import ABC, abstractmethod

class Procedure(ABC):
    @abstractmethod
    def Run() -> None:
        """Executes procedure. Procedure is the given set of instruction"""


class GenerateKeysProcedure(Procedure):
    def Run(self) -> None:
        GenerateKeys.Generate()