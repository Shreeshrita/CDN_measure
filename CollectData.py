import fetch_api
import time
import threading
url_list = [
    'https://www.hulu.com/watch/05e869d6-5a84-40c3-9c97-720c3a32d40a',
    'https://www.hulu.com/series/this-is-us-9dc170da-85db-475d-9df4-6572f15ffb00',
    'https://www.hulu.com/watch/0f7ed39a-0df8-415d-8c11-286caebdc8f9',
    'https://www.hulu.com/watch/b2cda97f-c8bf-4ef1-8f00-92432a87870c',
    'https://www.hulu.com/watch/5684da0d-fb27-4a11-b636-d1fe73bb2149'

]

suffix_list = ['Dulles:Chrome.DSL', 'Virginia:Chrome.DSL', 'Clifton:Chrome.DSL', 'NewYork:Chrome.DSL',
               'Orlando:Chrome.DSL', 'Chicago:Chrome.DSL']
csv_files = []
# index = 0
for suffix in suffix_list:
    for url in url_list:
        url1 = "http://www.webpagetest.org/runtest.php?url="+url+"&f=json&k=A.aada49748da06b441cef2a9cb402fd94&"+suffix
        # file = threading.Thread(target=fetch_api.get_csv, args=(url1))
        file = fetch_api.get_csv(url1)
        csv_files.append(file)
        print (file)
        time.sleep(5)

        # index += 1
    time.sleep(60)
    # for file in csv_files:
    #     cdn_server_list = fetch_api.decode_results(file)
    #     print (cdn_server_list)
    #

    print (fetch_api.decode_results(csv_files))