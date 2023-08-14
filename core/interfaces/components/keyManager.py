from abc import ABC, abstractmethod
from rsa import PublicKey, PrivateKey
import rsa


class KeyReader(ABC):
    @abstractmethod
    def ReadKey():
        """Return key"""
        ...


class KeyManager(ABC):
    @abstractmethod
    def does_public_key_exist() -> bool:
        """
        Checks if public key is in the directory.
        The directory set up in the settings.
        """
        ...
    
    @abstractmethod
    def does_private_key_exist() -> bool:
        """
        Check if private key is in the directory.
        The directory set up in the settings.
        """
        ...

    @abstractmethod
    def remove_public_key_from_dir() -> None:
        """
        Removes public key form the server.
        """
        ...
        
    @abstractmethod
    def remove_private_key_from_dir() -> None:
        """
        Removes private key form the server.
        """
        ...

    def save_keys_on_server() -> None:
        """
        Saves public and private keys on the server,
        The directory is set in the settings.
        """
        ...


class ReadPublicKeyFromFile(KeyReader):
    def ReadKey(self, key_filename: str) -> PublicKey:
        """
        Read RSA Public Key from file with .pem extension.
        Take as an argument key name as it is in the filesystem.
        """

        with open(key_filename, 'rb') as public_key:
            key_data = public_key.read()
        
        return rsa.PublicKey.load_pkcs1(key_data)
    

class ReadPrivateKeyFile(KeyReader):
    def ReadKey(self, key_filename: str) -> PrivateKey:
        """
        Read RSA Private Key from file with .pem extension.
        Take as an argument key name as it is in the filesystem.
        """

        with open(key_filename, 'rb') as private_key:
            key_data = private_key.read()
        
        return rsa.PrivateKey.load_pkcs1(key_data)
    

class KeySaver(KeyManager):
    def __init__(self) -> None:
        super().__init__()
        self.directory = None
    
    def save_keys_on_server(self, public_key: PublicKey, private_key: PrivateKey) -> None:
        pass