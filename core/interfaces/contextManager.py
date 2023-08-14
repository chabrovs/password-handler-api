from components import (
    csvManager, dbManager,
    keyManager, encryptor,
    errorLogger, generator,
    settingsReader
)

from abc import (
    ABC,
    abstractmethod,
    ABCMeta
)


class Context:
    """
    Define the interface of interest to client.
    Maintain reference to strategy object.  
    """

    def __init__(self, strategy) -> None:
        self._strategy = strategy

    def context_interface(self) -> None:
        self._strategy.algorithm_interface()


class Strategy(metaclass=ABCMeta):
    """
    Declare an interface common to all supported algorithms.
    Context uses this interface to call an algorithm defined by a 'Concrete Strategy'.
    """

    @abstractmethod
    def algorithm_interface(self):
        ...


class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using Strategy interface.
    """

    def algorithm_interface(self):
        return super().algorithm_interface()


class GenerateKeys(Strategy):
    def algorithm_interface(self):
        keys_length = settingsReader.Manager(
        ).settings_data['keysGenerator']['keysLength']
        generator.KeysGenerator(keys_length)


class GenerateKeysAndSaveAsFiles(Strategy):
    def algorithm_interface(self):
        """Generate public and private keys write them as PEM files"""
        keys_length = settingsReader.Manager().settings_data['keysGenerator']['keysLength']
        
        print(generator.KeysGenerator(keys_length).keys)


def main():
    generate_password = GenerateKeysAndSaveAsFiles()
    context = Context(generate_password)
    print(context.context_interface())


if __name__ == "__main__":
    main()
