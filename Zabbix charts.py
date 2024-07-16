# this script creates graphs based on recently added data items

import requests
import json
import matplotlib.pyplot as plt
import datetime

# API Configuration
ZABBIX_URL = 'http://your_zabbix_server/zabbix/api_jsonrpc.php'
ZABBIX_USER = 'your_username'
ZABBIX_PASSWORD = 'your_password'

def zabbix_api_call(method, params):
    headers = {'Content-Type': 'application/json'}
    payload = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'auth': auth_token,
        'id': 1
    }
    response = requests.post(ZABBIX_URL, headers=headers, data=json.dumps(payload))
    return response.json()

# Authorization
auth_payload = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'user': ZABBIX_USER,
        'password': ZABBIX_PASSWORD
    },
    'id': 1
}

response = requests.post(ZABBIX_URL, headers={'Content-Type': 'application/json'}, data=json.dumps(auth_payload))
auth_token = response.json()['result']

# Getting recently added data items
recently_added_items = zabbix_api_call('item.get', {
    'output': ['itemid', 'name', 'lastvalue', 'lastclock'],
    'sortfield': 'name',
    'sortorder': 'DESC',
    'limit': 10  # For example, the last 10 data items
})

if 'result' in recently_added_items:
    for item in recently_added_items['result']:
        item_id = item['itemid']
        item_name = item['name']

        # Getting the data history for an element
        history = zabbix_api_call('history.get', {
            'output': 'extend',
            'history': 0,  # Data type (0 - numeric floating point data)
            'itemids': item_id,
            'sortfield': 'clock',
            'sortorder': 'DESC',
            'limit': 100  # For example, the last 100 values
        })

        if 'result' in history:
            timestamps = [datetime.datetime.fromtimestamp(int(h['clock'])) for h in history['result']]
            values = [float(h['value']) for h in history['result']]

            # Creating a schedule
            plt.figure()
            plt.plot(timestamps, values, label=item_name)
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.title(f'Graph for {item_name}')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'graph_{item_id}.png')
            plt.close()
            print(f'Graph saved for item {item_name}')
else:
    print('Failed to retrieve recently added items.')

# Log out of the system
zabbix_api_call('user.logout', {})
