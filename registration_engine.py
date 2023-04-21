#! C:\Python311\python.exe

from validate_registration import validate_registration
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    email = sys.argv[3]
    value = validate_registration(username, password, email)
    print(value)