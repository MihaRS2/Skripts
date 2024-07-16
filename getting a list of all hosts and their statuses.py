# this script can be used to get information about all hosts registered with Zabbix, along with their current status.
from pyzabbix import ZabbixAPI

zabbix_server = 'http://your_zabbix_server/zabbix'
username = 'your_username'
password = 'your_password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)

hosts = zapi.host.get(output=['hostid', 'host', 'status'])
for host in hosts:
    status = 'Enabled' if host['status'] == '0' else 'Disabled'
    print(f"Host: {host['host']}, Status: {status}")
