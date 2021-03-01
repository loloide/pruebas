import requests, time
r = requests.post('http://localhost:8080/', json={"ts":time.time(), 'hello' : 'Anthony'})
print(r.status_code)
print(r.content)