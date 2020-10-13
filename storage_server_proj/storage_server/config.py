from os import environ

# Address of the main server to which the storage server will connect
NAME_SERVER_ADDRESS = environ.get("NAME_SERVER_ADDRESS", "http://name-server")

# Path in which files are stored to be checked for the free space
STORAGE_BASE_PATH = environ.get("STORAGE_BASE_PATH", "/home/vsftpd/")

# Address of the server to which this application is deployed
SERVER_ADDR = environ.get("SERVER_ADDR", "localhost")

# Port to which the http server is deployed
SERVER_PORT = environ.get("SERVER_PORT", "80")
