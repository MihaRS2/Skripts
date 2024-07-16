# This script can send custom notifications if certain triggers are triggered.
from pyzabbix import ZabbixAPI

zabbix_server = 'http://your_zabbix_server/zabbix'
username = 'your_username'
password = 'your_password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)

triggers = zapi.trigger.get(output=['triggerid', 'description'], filter={'value': 1})
for trigger in triggers:
    # Отправка кастомного уведомления
    print(f"Trigger {trigger['description']} is active!")
