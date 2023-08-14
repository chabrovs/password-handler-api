from abc import ABC, abstractmethod
from rsa import PublicKey, PrivateKey
import rsa

class Encryption(ABC):
    @abstractmethod
    def Encrypt() -> None:
        """Encrypts message."""
        ...
        

class Decryption(ABC):
    @abstractmethod
    def Decrypt() -> None:
        """Decrypt encrypted message."""
        ...


class PasswdEncryption(Encryption):
    def Encrypt(self, password: bytes, rsa_public_key: PublicKey) -> bytes:
        """Encrypts password with RSA public key."""
        
        return rsa.encrypt(password, rsa_public_key)


class PasswdDecryption(Decryption):
    def Decrypt(self, password: bytes, rsa_private_key: PrivateKey) -> bytes:
        """Decrypt encrypted message by RSA private key"""
        
        return rsa.decrypt(password, rsa_private_key)