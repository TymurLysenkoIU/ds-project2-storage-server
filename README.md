# Deployment

## Configuration

There is a python configuration file for the application located at `storage_server_proj/storage_server/config.py`. Check it to configure the address of the name server to which the storage server instance will connect and other settings.

### Environment variables

- `DJANGO_SECRET_KEY` - secret key to be used for the application
- `STORAGE_BASE_PATH` - path in which files are stored to be checked for the free space (default is `/home/vsftpd/`)
- `NAME_SERVER_ADDRESS` - address of the main server to which the storage server will connect (default is `http://name-server`)

## Docker

### Build docker image

From the current folder run:

```sh
docker build --tag sitiritis/ds-dfs-storage-server -f ./docker/Dockerfile .
```

### Run a container

This image is based on [vsftpd](https://hub.docker.com/r/fauria/vsftpd/) image, so check its documentation to specify configuration and map ports for the FTP server.

The API will be available to port **80**, so this port of the container has to be mapped to some port on the host operating system.

Sample command to run:

```sh
docker run -p 8000:80 -p 20:20 -p 21:21 -p 21100-21110:21100-21110 -e "PASV_MIN_PORT=2100" -e "PASV_MAX_PORT=21110" --name storage-server sitiritis/ds-dfs-storage-server
```


