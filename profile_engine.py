#! C:\Python311\python.exe

from retrieve_profile import retrieve_profile
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    value = retrieve_profile(username)
    print(value)