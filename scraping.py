import requests

url = "http://www.fb.com"

response = requests.get(url)
f = open("e:\\scraping.txt",'wb')
for data in response.iter_content(10000):
    f.write(data)
f.close()


