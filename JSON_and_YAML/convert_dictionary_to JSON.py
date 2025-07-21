# create the dictionary

import json

servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# json_string = json.dumps(servers_dict, indent = 4)
# print(json_string)
# print(type(servers_dict))

with open('servers.json', 'w') as f:
    json.dump(servers_dict, f, indent = 4)