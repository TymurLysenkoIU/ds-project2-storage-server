#!/bin/bash
/usr/sbin/run-vsftpd.sh &

(
  cd /storage-server && \
    daphne \
    -b 0.0.0.0 -p 80 \
    storage_server_proj.asgi:application
)
