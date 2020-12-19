#Parse the html usinf Regular expressions

import urllib.request
import ssl
import re

#enter host name
hostname=input("Enter :")

#Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(hostname, context=ctx).read()


list = re.findall(b'href="(http[s]?://.*?)"',data)
print("check", len(list))
for link in list:
    print(link.decode())
    