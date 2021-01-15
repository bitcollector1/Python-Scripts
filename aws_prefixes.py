import requests
import json 

r = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
d = r.json() 

ip_prefix_list = d.get("prefixes")

for i in ip_prefix_list:
   ip = i.get("ip_prefix")
   print (ip)

