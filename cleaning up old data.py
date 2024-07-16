# This script can be used to delete old data from Zabbix

from pyzabbix import ZabbixAPI

zabbix_server = 'http://your_zabbix_server/zabbix'
username = 'your_username'
password = 'your_password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)

days_old = 30
time_till = int(time.time()) - (days_old * 24 * 60 * 60)

items = zapi.item.get(output=['itemid'])
for item in items:
    zapi.history.delete(itemids=[item['itemid']], time_till=time_till)
print(f"Data older than {days_old} days has been deleted")
