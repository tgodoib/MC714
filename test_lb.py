import requests
import time

ip = ''

requests_total = 10
interval_seconds = 1

count = {
    'sv-01': 0,
    'sv-02': 0,
}

for i in range(requests_total):
    x = requests.get(f'http://{ip}/')
    count[x.text] += 1

    print(x.text)
    time.sleep(interval_seconds)

print(count)
