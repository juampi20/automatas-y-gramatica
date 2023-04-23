import re

patron = r'^((\d|\d\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|\d\d|1\d\d|2[0-4]\d|25[0-5])$'
# \d = [0-9]
# \d\d = [0-9][0-9]
# 1\d\d = 1[0-9][0-9]
# 2[0-4]\d = 2[0-4][0-9]
# 25[0-5]

ips = [
    '192.168.1.8',
    '0.0.0.0',
    '255.255.255.255',
    '1.1.1.1',
    '256.198.1.1',
    '192.255.192.1',
    '19.192.126.1'
]

for ip in ips:
    if re.match(patron, ip):
        print(f'{ip} es una IP válida')
    else:
        print(f'{ip} no es una IP válida')
