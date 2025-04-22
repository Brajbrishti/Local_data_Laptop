import requests
import bs4

URL ="http://www.fb.com"

response =requests.get(URL)

parsed_data =bs4.BeautifulSoup(response.text)

all_links =parsed_data.select('a')
#print(len(all_links))
for l in all_links:

    print(l.get("href"))
    print("title =:",l.get('title'))

