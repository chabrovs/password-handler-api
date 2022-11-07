# WHAT IS # password-handler-api
Generate strong passwords and use encryption to handle them (Store, etc.)
Password Handler public API. Great for web applications.


# HOW TO USE.
### AS CMD application:
  1. Download password_generator.py
  2. move password_generator.py to the working directory.
  3. run command `python3 password_generator.py -g` to generate public and private keys.
  4. run command `python3 password_generator.py` then type name into the input field for the newly generating password. For example: google_accaunt and PRESS Enter.
  5. run command `python3 password_generator.py -f <name>` to lay out the decrypted password.

### AS a API:
  1. Download password_generator.py
  2. move password_generator.py to the working directory.
  3. run command `python3 password_generator.py -g` to generate public and private keys.
  4. Import the APIRequestsHandler into your file. Ex (from … import apiRequestsHandler)
  5. Open the source file (password_generator.py). Use the class APIRequestsHandler in your code.

#### Class APIRequestHandler methods guide

  Function | Description
------------ | -------------
api_get_records_form_csv() -> dict[str] | Returns all records from the csv file.
api_generate_password_for(name: str) -> None | Generates and saves password to csv file with Name and Password columns.
api_find_password(name: str) -> dict[Any, Any] (str) | It Looks for the password. In a successful case, it returns the decrypted password.
api_get_public_key() -> str | It returns public key from ‘publick_key.pem’ in bytes | str
api_generate_new_keys(safe=True) -> None | It generates new RSA encryption keys.  

***use `python3 password_generator.py -?` for help***

# HOW IT WORKS.
Generate a strong password using the "pandas.choices.random" module.
Then encrypts the password using the RSA module, and encodes the encrypted password into base.b64encode. Then stared encrypted password along with its name (name is not encrypted) in CSV file "passwords.csv".
