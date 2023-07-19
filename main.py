import os
from sys import argv


def main():
    try:
        from passwdHandler.management import execute_from_command_line
    except Exception as exp:
        print(f"Launching error: {exp}")
    
    execute_from_command_line


def api_service():
    try:
        from passwdHandler.management import execute_api_requests
    except Exception as exp:
        print(f"Launching error: {exp}")

if __name__ == "__main__":
    print(f"{os.path.basename(__file__)} started as an independent program. Name {__name__}")
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        pass
else:
    apiRequestsHandler = APIRequestsHandler()
    print(f"{os.path.basename(__file__)} started as a API. Name: {__name__}")