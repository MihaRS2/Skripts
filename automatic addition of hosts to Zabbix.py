# This script can automatically add new hosts to Zabbix using AP
from pyzabbix import ZabbixAPI

zabbix_server = 'http://your_zabbix_server/zabbix'
username = 'your_username'
password = 'your_password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)

new_host = {
    'host': 'new_host_name',
    'interfaces': [
        {
            'type': 1,
            'main': 1,
            'useip': 1,
            'ip': '192.168.1.1',
            'dns': '',
            'port': '10050'
        }
    ],
    'groups': [
        {
            'groupid': '2'
        }
    ],
    'templates': [
        {
            'templateid': '10001'
        }
    ]
}

zapi.host.create(new_host)
print("Host added successfully")
