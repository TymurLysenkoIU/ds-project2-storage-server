FROM fauria/vsftpd:latest

# install python
RUN yum update -y &&\
    yum install -y python3

# Make declarations and copy the entrypoint script, because it doesn't change often,
# so the earlear this is done, the faster subsequent builds will be, when source code
# of the application changes
ENV LANG="en_US.utf8"
ENV LANGUAGE="en_US:en"
ENV LC_ALL="en_US.utf8"

EXPOSE 80

COPY ./docker/storage-server-entrypoint.sh /usr/sbin/
RUN chmod +x /usr/sbin/storage-server-entrypoint.sh

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Declare environment variables for the application
ENV DJANGO_SECRET_KEY="set_your_secret"
ENV STORAGE_BASE_PATH="/home/vsftpd/"
ENV NAME_SERVER_ADDRESS="http://name-server"

# Copy the application to the image
COPY ./storage_server_proj /storage-server/storage_server_proj
COPY ./docker/settings.py /storage-server/storage_server_proj/
# Copy static files
COPY ./manage.py /storage-server/
RUN cd /storage-server/ && python3 manage.py collectstatic --noinput
# nginx needs to be configured to serve static files, but is not needed for now

ENTRYPOINT ["/usr/sbin/storage-server-entrypoint.sh"]
