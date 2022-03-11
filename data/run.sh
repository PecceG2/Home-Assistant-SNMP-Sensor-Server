#!/usr/bin/with-contenv bashio

bashio::log.info "Preparing SNMP Sensor Server, please wait.."
CONFIG="/etc/snmp/snmpd.conf"

{
	echo "com2sec readonly default $(bashio::config 'community')"
	echo "syslocation $(bashio::config 'location')"
	echo "syscontact $(bashio::config 'name') <$(bashio::config 'email')>"
	echo "group MyROGroup v2c readonly"
	echo "view all included .1 80"
	echo "access MyROGroup ''      any       noauth    exact  all    none   none"
} > "${CONFIG}"


if bashio::var.true "$(bashio::config 'expose_sensors')"; then
	bashio::log.info "Generating OID for HA sensors.."
	OUTPUT=$(python3 snmpd-configurator.py ${CONFIG} "$(bashio::config 'expose_sensors_OID_base')")
	bashio::log.info "${OUTPUT}"
fi


bashio::log.info "Listening SNMP Sensor Server..."
exec /usr/sbin/snmpd \
	-c "${CONFIG}" \
	-f \
	< /dev/null
