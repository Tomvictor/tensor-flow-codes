import urllib.request as req
import json

TEST_URL = "https://buildfromzero.com/tutorials/search/"


with req.urlopen(TEST_URL) as f:
    data = f.read()
print(data)
response = data.decode('utf-8')
data = json.loads(response)
print(data)
