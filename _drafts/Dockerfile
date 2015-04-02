FROM ubuntu:14.10
MAINTAINER seems <529574002@qq.com>

# install postgresql & postgis in the docker
RUN apt-get update && apt-get install -y vim postgresql postgresql-9.4-postgis-2.1 postgresql-9.4-postgis-2.1-scripts postgresql-9.4-postgis-scripts postgresql-contrib

USER postgres

RUN echo "host all all    0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf

RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf

RUN /etc/init.d/postgresql start

# Enable postgis exthensions on new database
RUN psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';"

# Add volumes to allow backup for config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# CREATE EXTENSION postgis;
# CREATE EXTENSION postgis_topology;
# CREATE EXTENSION fuzzystrmatch;
# CREATE EXTENSION postgis_tiger_geocoder;

# docker run -it --name postgis -v /home/panlei/db_data:/var/lib/postgresql/9.4/main seems/postgres:9.4 /bin/bash



