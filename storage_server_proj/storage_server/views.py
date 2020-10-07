from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import rest_framework.status as status

from .config import STORAGE_BASE_PATH

import shutil


class PingView(APIView):
  def get(self, request: Request) -> Response:
    return Response()


class SpaceView(APIView):
  def get(self, request: Request) -> Response:
    try:
      return Response(data={
        # "bytes_free": shutil.disk_usage(".").free,
        "bytes_available": shutil.disk_usage(STORAGE_BASE_PATH).free,
      })
    except:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
