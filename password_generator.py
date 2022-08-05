import csv
import os
import sys
import rsa
import base64
import pandas as pd
import numpy as np
from datetime import datetime


DESCRIPTION = {
    '': 'Password handler. Encrypts and stored password in CSV file.',
    '-r': ' Read all data from csv file',
    '-f name': ' Return decrypted password. (Example: -f google.com)',
    '-g': ' Generate keys',
    '-pub_key': ' Show public key',
    '-priv_key': ' Show private key',
    '?': ' For help'
}


class DebugUtils:
    def timer(self, func_name: str):
        "Decorator to measure time complexity"
        def outer(func):
            def wrapper(*args, **kwargs):
                started = datetime.now()
                result = func(*args, **kwargs)
                print(f"{func_name} has taken: {datetime.now() - started}")
                return result
            return wrapper
        return outer


debug_utils = DebugUtils()


class Generate:
    data = {
        'letters_lowercase': "abcdefghijklmnopqrstuvwxyz",
        'letters_uppercase': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        'numbers': "0123456789",
        'symbols': "!@#$%^*"
    }

    def __init__(self, length=32, replace=True) -> None:
        super(Generate, self).__init__()
        self.length = length
        self.replace = replace
        self._data_to_use = self.data['letters_lowercase'] + \
            self.data['letters_uppercase'] + \
            self.data['numbers'] + self.data['symbols']

    def generate_password(self) -> str:
        result = np.random.choice(
            [char for char in self._data_to_use], size=self.length, replace=self.replace)
        result = "".join(result)

        return result


class Cryptography:
    def __init__(self) -> None:
        super(Cryptography, self).__init__()
        self._private_key_filename = 'private_key.pem'
        self._public_key_filename = 'public_key.pem'
        self._cwd = os.getcwd()

    @staticmethod
    def save_keys(func):
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            public_key, private_key = results
            to_save = [(public_key.save_pkcs1(format='PEM'), args[0]._public_key_filename),
                       (private_key.save_pkcs1(format='PEM'), args[0]._private_key_filename)]

            for key, filename in to_save:
                with open(args[0]._cwd + '\\' + filename, 'wb') as f:
                    f.write(key)
                f.close()

            return results
        return wrapper

    @save_keys
    def generate_keys(self) -> tuple[bytes, bytes]:
        (public_key, private_key) = rsa.newkeys(512)
        return (public_key, private_key)

    def read_public_key(self) -> rsa.PublicKey:
        with open(self._public_key_filename, 'rb') as public_file:
            keydata = public_file.read()
        return rsa.PublicKey.load_pkcs1(keydata)

    def read_private_key(self) -> rsa.PrivateKey:
        with open(self._private_key_filename, 'rb') as private_file:
            keydata = private_file.read()
        return rsa.PrivateKey.load_pkcs1(keydata)

    def encrypt(self, message: str) -> bytes:
        return rsa.encrypt(message, self.read_public_key())

    def decrypt(self, encrypted_message: bytes) -> str:
        return rsa.decrypt(encrypted_message, self.read_private_key())


class Save_to_file(Generate, Cryptography):
    _field_names = ['name', 'password']

    def __init__(self) -> None:
        super(Save_to_file, self).__init__()
        self._filename = 'passwords.csv'
        self.__cwd = os.getcwd()

    def is_empty(self) -> bool:
        if os.path.getsize(self.__cwd + '\\' + self._filename) == 0:
            return True

        return False

    def save_records_to_csv(self, name: str, unique_name_field=True) -> None:
        if unique_name_field:
            data = self.read_records_from_csv()
            for name_field in data.items():
                if name in name_field:
                    name = name + 'copy_(1)'
            name = str(name).lower()
            value = base64.b64encode(self.encrypt(
                self.generate_password().encode('utf8'))).decode()
            values = [name, value]
            with open(self._filename, 'a', newline='') as file:
                writer = csv.writer(file)
                if self.is_empty():
                    writer.writerow(self._field_names)
                else:
                    writer.writerow(values)

                file.close()
        else:
            raise Exception(
                ('Please, set the "unique_name_field" attribute of "save_records_to_csv" function to "True"'))

    def read_records_from_csv(self) -> dict[str, str]:
        data = {}
        with open(self._filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',',
                                quotechar='|', doublequote=False, escapechar='')
            for row in reader:
                data[row[0]] = row[1]
            file.close()
        return data

    def show_password(self, name) -> dict[str, str]:
        data = self.read_records_from_csv()
        for key, value in data.items():
            if key == name:
                password = base64.b64decode(value)
                return {name: self.decrypt(password).decode()}
        return {name: 'Was not found!'}

    def read_csv_pandas(self) -> pd.DataFrame:
        return pd.read_csv(self._filename)

    def delete_row_from_csv(self, name):
        df = self.read_csv_pandas()
        df.dropna(inplace=True)
        a = df["Indexes"] = df["Name"].str.find(name)
        print(a)
        # print(df.loc[df['name'].str.contains(name)])


class APIRequestsHandler(Save_to_file):
    def __init__(self) -> None:
        super(APIRequestsHandler, self).__init__()

    def api_get_records_from_csv(self) -> dict[str]:
        "Returns all records from csv file"
        return self.read_records_from_csv()

    def api_generate_password_for(self, name: str) -> None:
        "Generates and saves password to csv file with Name and Password columns"
        self.save_records_to_csv(name)
        return None

    def api_find_password(self, name: str) -> tuple[str]:
        "Looks for the password. In a succeed case, return a decrypted password. (Pass name of the required query without additional args)"
        return self.show_password(name.lower())

    def api_get_public_key(self) -> str:
        "Return public key from 'public_key.pem' in bytes"
        return str(self.read_public_key())

    def api_generate_new_keys(self, safe=True) -> None:
        "Generated new RSA encryption keys via safe generation method"
        if safe:
            if os.path.isfile(self._cwd + '\\' + self._public_key_filename) or os.path.isfile(self._cwd + '\\' + self._private_key_filename):
                print("""
                    Attention!\n Keys are already exist!
                    \n Before generation new keys, make sure to save existing keys. Otherwise, you can lose access to yours' encrypted passwords!\n""")
                decision = str(
                    input("'Y' to generate new keys or 'N' to exit: ")).upper()
                if decision == 'Y':
                    self.generate_keys()
                elif decision == 'N':
                    raise KeyboardInterrupt
            else:
                self.generate_keys()

        return self.generate_keys()


def main():
    save_to_file = Save_to_file()
    if len(sys.argv) > 1:
        if '-r' in sys.argv:
            print(save_to_file.read_records_from_csv())
        elif '-g' in sys.argv[1]:
            # Safe key generation
            cryptography = Cryptography()
            if os.path.isfile(cryptography._cwd + '\\' + cryptography._public_key_filename) or os.path.isfile(cryptography._cwd + '\\' + cryptography._private_key_filename):
                print("""
                Attention!\n Keys are already exist!
                \n Before generation new keys, make sure to save existing keys. Otherwise, you can lose access to yours' encrypted passwords!\n""")
                decision = str(
                    input("'Y' to generate new keys or 'N' to exit: ")).upper()
                if decision == 'Y':
                    cryptography.generate_keys()
                elif decision == 'N':
                    raise KeyboardInterrupt
            else:
                cryptography.generate_keys()
        elif '-f' in sys.argv[1]:
            save_to_file.show_password(sys.argv[2].lower())
        elif '-d' in sys.argv[1]:
            save_to_file.delete_row_from_csv(sys.argv[2].lower())
        elif '-pub_key' in sys.argv[1]:
            cryptography = Cryptography()
            print(cryptography.read_public_key())
        elif '-priv_key' in sys.argv[1]:
            cryptography = Cryptography()
            print(cryptography.read_private_key())
        elif '?' or 'help' in sys.argv:
            for key, value in DESCRIPTION.items():
                print(key, value)
    else:
        save_to_file.save_records_to_csv()


# Not used with API
# if __name__ == "__main__":
#     try:
#         # main()
#         # api_requests_handler(['-r'])
#         pass
#     except (KeyboardInterrupt, SystemExit):
#         pass
