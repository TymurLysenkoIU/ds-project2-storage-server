from django.apps import AppConfig

import sys

import requests as r

from .config import NAME_SERVER_ADDRESS


class StorageServerConfig(AppConfig):
  name = 'storage_server_proj.storage_server'

  def ready(self):
    try:
      # TODO: when the endpoint will be implemented get back to this place
      # r.get(
      #   url=f"{NAME_SERVER_ADDRESS}/connect",
      #   params={},
      # )
      pass
    except:
      print(f"Unable to connect to the name server: {NAME_SERVER_ADDRESS}")
      print("Exiting...")
      sys.exit(1)
