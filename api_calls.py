import csv
import urllib.request
import codecs
import pandas as pd
import json
import time

url1 = "http://www.webpagetest.org/runtest.php?url=https://www.hulu.com/watch/05e869d6-5a84-40c3-9c97-720c3a32d40a&f=json&k=A.aada49748da06b441cef2a9cb402fd94"
jsonres = urllib.request.urlopen(url1)
res_body = jsonres.read()
# This json response holds the location of link (inside data.detailsCSV) where results are there.
jsonresponse = json.loads(res_body.decode("utf-8"))
print(jsonresponse)
url2 = str(jsonresponse["data"]["detailCSV"])
testId = str(jsonresponse["data"]["testId"])
#print(url2)
#print(testId)

# Check whether the test results are available
while (1):
    url3 = "http://www.webpagetest.org/testStatus.php?f=json&test=" + testId
    jsonres1 = urllib.request.urlopen(url3)
    res_body1 = jsonres1.read()
    jsonresponse1 = json.loads(res_body1.decode("utf-8"))
    print(jsonresponse1)
    testStatus = str(jsonresponse1["statusCode"])
    if testStatus == "200":
        break
    time.sleep(30)

ftpstream = urllib.request.urlopen(url2)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

# If one wants to store csv file in pandas dataframe
df = pd.read_csv(ftpstream)
#print(df.head(2))