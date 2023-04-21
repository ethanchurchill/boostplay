#! C:\Python311\python.exe

from validate_login import validate_login
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    value = validate_login(username, password)
    print(value)