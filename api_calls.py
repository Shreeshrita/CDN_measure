import csv
import urllib.request
import codecs
import pandas as pd
import json

url1 = "http://www.webpagetest.org/runtest.php?url=www.google.com&f=json&k=A.aada49748da06b441cef2a9cb402fd94"
jsonres = urllib.request.urlopen(url1)
res_body = jsonres.read()
jsonresponse = json.loads(res_body.decode("utf-8"))
print(jsonresponse)
url2 = str(jsonresponse["data"]["detailCSV"])
print(url2)
'''
ftpstream = urllib.request.urlopen("http://www.webpagetest.org/result/181106_EQ_84ff037213173a959ac117de08de20b7/requests.csv")
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
i = 0
for line in csvfile:
    if (i==2):
        break
    i += 1
    print(line)

df = pd.read_csv(ftpstream)
print(df.head(2))
'''