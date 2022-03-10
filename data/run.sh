#!/usr/bin/with-contenv bashio

function get_sensor_data() {
  local sensor_id=${1}
  local sensor_data
  return "${__BASHIO_EXIT_OK}"
}

CONFIG="/etc/snmp/snmpd.conf"

{
	echo "com2sec readonly default $(bashio::config 'community')"
	echo "syslocation $(bashio::config 'location')"
	echo "syscontact $(bashio::config 'name') <$(bashio::config 'email')>"
	echo "group MyROGroup v2c readonly"
	echo "view all included .1 80"
	echo "access MyROGroup ''      any       noauth    exact  all    none   none"
} > "${CONFIG}"

bashio::log.info "Getting sensors from HA API..."
bashio::log.info "$(bashio::api.supervisor 'GET' '/api/states')"

bashio::log.info "Starting SNMP server..."
exec /usr/sbin/snmpd \
	-c "${CONFIG}" \
	-f \
	< /dev/null
