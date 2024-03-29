ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY data/* /
RUN chmod a+x /run.sh
RUN chmod a+x /get-sensor-data-pyconvert.sh

# Install requirements for add-on
RUN apk add --no-cache net-snmp net-snmp-tools py3-pip python3 python3-dev

# So let's set it to our add-on persistent data directory.

CMD [ "/run.sh" ]
