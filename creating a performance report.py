# this script can generate a performance report for a specific period for a given host.
from pyzabbix import ZabbixAPI

zabbix_server = 'http://your_zabbix_server/zabbix'
username = 'your_username'
password = 'your_password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(username, password)

host_id = '10105'
item_key = 'system.cpu.load[all,avg1]'
time_from = 1633024800
time_till = 1633111200

items = zapi.item.get(filter={'hostid': host_id, 'key_': item_key})
if not items:
    print("Item not found")
    exit()

item_id = items[0]['itemid']
history = zapi.history.get(itemids=[item_id], time_from=time_from, time_till=time_till, output='extend', sortfield='clock', sortorder='ASC')

for record in history:
    print(f"Time: {record['clock']}, Value: {record['value']}")
