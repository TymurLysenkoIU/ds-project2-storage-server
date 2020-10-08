from os import environ

# Address of the main server to which the storage server will connect
NAME_SERVER_ADDRESS = environ.get("NAME_SERVER_ADDRESS", "http://name-server")

# Path in which files are stored to be checked for the free space
STORAGE_BASE_PATH = environ.get("STORAGE_BASE_PATH", "/home/vsftpd/")
