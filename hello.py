from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import json


def main():
    req = Request(
        url="https://glints.com/id/opportunities/jobs/explore?country=ID&locationName=All%20Cities%2FProvinces",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    webpage = urlopen(req)
    data_html = bs(webpage.read(), "html.parser")
    data_job = data_html.find_all("script", {"id": "__NEXT_DATA__"})[0].get_text()
    json_data_job = json.loads(data_job)
    json_data_job = json.dumps(json_data_job)
    
    with open('glints.json','w') as outfile:

        outfile.write(json_data_job)


if __name__ == "__main__":
    main()
