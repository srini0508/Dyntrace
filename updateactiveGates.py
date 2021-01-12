import requests,json
requests.packages.urllib3.add_stderr_logger()
agId = []
import sys
url="https://plg31677.live.dynatrace.com/api/v2/activeGates/"
api='Api-Token' + " " + sys.argv[1]
print(api)
headers = {
    'Authorization': api,
    'Content-Type': 'application/json',
   }

   

response = requests.get('https://plg31677.live.dynatrace.com/api/v2/activeGates/', headers=headers)

   
response_dict = json.loads(response.text)
todos = json.loads(response.text)
#print(response_dict.keys())
y=json.dumps(response_dict, indent = 2)
#print(type(y))
xstr=json.loads(y)
ab=xstr["activeGates"]
#print (type(xstr))
#print (type(ab))

for i in ab:
        print(i["id"])
        #agId.append=i["id"]
        url=url+i["id"]+"/updateJobs/"
        print(url)
        data = '{ "targetVersion": "latest" }'
        sendupdate = requests.post(url, headers=headers, data=data)
        url="https://plg31677.live.dynatrace.com/api/v2/activeGates/"
        print(sendupdate.text)

