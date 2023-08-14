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


class KeysGenerator(Generator):
    def __init__(self, key_size: int) -> None:
        super().__init__()
        self.key_size = key_size
        self.keys: tuple = self.Generate()

    def Generate(self) -> tuple[PublicKey, PrivateKey]:
        """Generates public and private RSA keys"""
        public_key, private_key= rsa.newkeys(self.key_size)
        print(public_key, private_key)
        return public_key, private_key
