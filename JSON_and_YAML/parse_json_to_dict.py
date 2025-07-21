import json

with open("servers.json", "r") as file:
    servers = json.load(file)

print(type(servers))

print("server1 record", servers["server1"])
print("server2 record", servers["server2"])

for key, value in servers.items():
    print(key, value)

# when something has to bne parsed it has to break it down into the data components
# usually is stored in a data structure
# serialise is the opposite of parse
