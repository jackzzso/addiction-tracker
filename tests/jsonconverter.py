import json

USERNAME = ''
UUID = ''
HASH = ''
TOKEN = ''
ACCTYPE = ''
TIMESTAMP = ''

data = {
    USERNAME: {
        'UUID': UUID,
        'HASH': HASH,
        'TOKEN': TOKEN,
        'ACCTYPE': ACCTYPE,
        'TIMESTAMP': TIMESTAMP
    }
}

j = json.dumps(data)
print(j)
