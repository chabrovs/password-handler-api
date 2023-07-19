from abc import ABC, abstractmethod
from rsa import PublicKey, PrivateKey
import rsa

class Generator(ABC):
    @abstractmethod
    def Generate() -> str:
        """Generates string of random characters depending on passed settings."""
        ...


class PasswordGenerator(Generator):
    def Generate(self) -> str:
        """
        Generate string of random characters depending on passed settings.
        Generates password.
        """
        ...
    

class SuffixGenerator(Generator):
    def Generate(self) -> str:
        """
        Generate string of random characters depending on passed settings.
        Generates suffix for unique filename.
        """
        ...


class FilenameGenerator(Generator):
    def Generate(self) -> str:
        """
        Generates unique filename depending on passed settings.
        """
        suffix = SuffixGenerator.Generate()
        ...


class GenerateKeys(Generator):
    def __init__(self, nbits=None) -> None:
        super().__init__()
        if nbits == None:
            nbits = 512
            
        self.nbits: int = nbits

    def Generate(self) -> tuple[PublicKey, PrivateKey]:
        """
        Generates public and private RSA keys depending on passed settings.
        """
        (public_key, private_key) = rsa.newkeys(self.nbits)
        
        return public_key, private_key