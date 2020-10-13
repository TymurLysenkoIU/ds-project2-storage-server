from django.apps import AppConfig

import sys

import requests as r

from .config import NAME_SERVER_ADDRESS, SERVER_ADDR, SERVER_PORT


class StorageServerConfig(AppConfig):
  name = 'storage_server_proj.storage_server'

  def ready(self):
    if ('collectstatic' not in sys.argv):
      try:
        r.get(
          url=f"{NAME_SERVER_ADDRESS}/connect",
          params={
            "addr": SERVER_ADDR,
            "port": SERVER_PORT,
          },
        )
      except Exception as e:
        print(f"Unable to connect to the name server: {NAME_SERVER_ADDRESS}")
        print(f"Error: {e}")
        print("Exiting...")
        sys.exit(1)
