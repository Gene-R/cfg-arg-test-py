#!/usr/bin/env python3
import appconfig
import appargs
import http.client


args = appargs.AppArgs().args
cfg = appconfig.AppConfig(args.env)

print('... env host: ' + cfg.env['host'])

conn = http.client.HTTPConnection(cfg.env['host'])
conn.set_debuglevel(10)
conn.request("POST", "/session")
response  = conn.getresponse()
print(response.status, response.reason)
print(response.read())
conn.close()

# url = 'https://github.com/session'
# data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
# params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
# requests.post(url, params=params, json=data)


